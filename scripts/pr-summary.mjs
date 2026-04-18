#!/usr/bin/env node

import fs from 'fs'
import path from 'path'
import { execFileSync } from 'child_process'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)
const PROJECT_ROOT = path.resolve(__dirname, '..')

const CATEGORY_RULES = [
  { name: 'source', match: file => file.startsWith('raw/') },
  { name: 'asset', match: file => file.startsWith('assets/') },
  { name: 'output', match: file => file.startsWith('output/') },
  { name: 'wiki', match: file => file.startsWith('wiki/') },
  { name: 'publish-contract', match: file => file === 'docs/publishing-contract.md' || file.includes('publish') },
  { name: 'script', match: file => file.startsWith('scripts/') || file.startsWith('.claude/commands/wiki/') },
  { name: 'agent-surface', match: file => file === 'AGENTS.md' || file === 'CLAUDE.md' || file.startsWith('.claude/') || file.startsWith('.codex/') },
  { name: 'docs', match: file => file.startsWith('docs/') || file === 'README.md' },
  { name: 'test', match: file => file.startsWith('tests/') || file.endsWith('.test.py') },
]

const REVIEW_QUESTIONS = [
  '이 변경이 wiki source-of-truth 경계를 흐리는가',
  'publish contract 또는 downstream 호환성을 깨는가',
  'wiki/index.md, wiki/log.md, tags 동기화가 필요한가',
  '문서와 실제 운영 모델 설명이 어긋나는가',
  '완료 전에 wiki lint나 publish 검증이 더 필요한가',
]

function parseArgs(argv) {
  const args = { files: [], output: '' }

  for (let i = 2; i < argv.length; i += 1) {
    const current = argv[i]
    const next = argv[i + 1]

    if (current === '--base' && next) {
      args.base = next
      i += 1
      continue
    }
    if (current === '--head' && next) {
      args.head = next
      i += 1
      continue
    }
    if (current === '--files' && next) {
      args.files = next.split(',').map(item => item.trim()).filter(Boolean)
      i += 1
      continue
    }
    if (current === '--output' && next) {
      args.output = next
      i += 1
    }
  }

  return args
}

function getChangedFiles(args) {
  if (args.files.length > 0) return args.files

  if (args.base && args.head) {
    const output = execFileSync('git', ['diff', '--name-only', `${args.base}...${args.head}`], {
      cwd: PROJECT_ROOT,
      encoding: 'utf-8',
    }).trim()
    return output ? output.split('\n').map(line => line.trim()).filter(Boolean) : []
  }

  const output = execFileSync('git', ['status', '--porcelain', '--untracked-files=all'], {
    cwd: PROJECT_ROOT,
    encoding: 'utf-8',
  }).trim()

  if (!output) return []

  return output
    .split('\n')
    .map(line => line.slice(3).trim())
    .filter(Boolean)
}

function categorize(files) {
  const categories = new Set()

  for (const file of files) {
    for (const rule of CATEGORY_RULES) {
      if (rule.match(file)) categories.add(rule.name)
    }
  }

  return [...categories]
}

function inferRisk(categories) {
  if (categories.includes('publish-contract')) return 'high'
  if (categories.includes('wiki') && categories.includes('script')) return 'high'
  if (categories.includes('agent-surface') && categories.includes('docs')) return 'medium'
  if (categories.includes('wiki') || categories.includes('script')) return 'medium'
  if (categories.every(category => ['source', 'asset', 'output', 'docs', 'test'].includes(category))) return 'low'
  return 'medium'
}

function summarize(files, categories) {
  if (files.length === 0) return '변경 파일을 찾지 못해 요약을 생성하지 못함'
  if (categories.includes('wiki') && categories.includes('publish-contract')) {
    return 'wiki 내용과 publish contract 경로를 함께 수정'
  }
  if (categories.includes('source') && categories.includes('wiki')) {
    return '원본 자료 계층과 wiki 지식층을 함께 수정'
  }
  if (categories.includes('asset') || categories.includes('output')) {
    return '제작 자산 또는 산출물 경로를 수정'
  }
  if (categories.includes('agent-surface')) {
    return '에이전트 운영 표면과 문서를 수정'
  }
  if (categories.includes('script')) {
    return 'wiki 운영 스크립트 또는 커맨드 경로 수정'
  }
  if (categories.includes('docs')) {
    return '운영/계약 문서 수정'
  }
  return `${files.length}개 파일 변경`
}

function buildVerification(categories) {
  const lines = []
  const checks = []

  if (categories.includes('wiki') || categories.includes('script')) {
    lines.push('wiki 구조 또는 자동화 경로 변경 있음')
    checks.push('python3 scripts/wiki lint --summary')
  }
  if (categories.includes('publish-contract')) {
    lines.push('publish contract 영향 가능성 있음')
  }
  if (categories.includes('agent-surface') || categories.includes('docs')) {
    lines.push('문서와 운영 규칙 정합성 확인 필요')
  }
  if (categories.includes('test')) {
    lines.push('테스트 파일 변경 있음')
  }

  if (checks.length > 0) {
    lines.push(`확인 권장: ${[...new Set(checks)].join(', ')}`)
  }

  return lines.length > 0 ? lines : ['추가 검증 필요 여부를 수동 확인']
}

function buildReviewPoints(files, categories) {
  const points = []

  if (categories.includes('source')) {
    points.push('raw/가 불변 원본 보존 원칙을 깨지 않았는지 확인')
  }
  if (categories.includes('asset')) {
    points.push('assets/가 문서 계층과 섞이지 않고 채널별 경계를 유지하는지 확인')
  }
  if (categories.includes('output')) {
    points.push('output/blog 산출물이 최종 downstream content/posts 계약과 혼동되지 않는지 확인')
  }
  if (categories.includes('wiki')) {
    points.push('wiki/index.md, wiki/log.md, 관련 역링크 반영이 필요한지 확인')
  }
  if (categories.includes('publish-contract')) {
    points.push('downstream content/posts 경로와 frontmatter 계약이 유지되는지 확인')
  }
  if (categories.includes('script')) {
    points.push('wiki lint/sync/publish 동작 경로가 기존 운영 모델과 충돌하지 않는지 확인')
  }
  if (categories.includes('agent-surface')) {
    points.push('README.md, AGENTS.md, CLAUDE.md, .claude/.codex 설명이 같은 경계를 말하는지 확인')
  }
  if (files.some(file => file === 'wiki/index.md' || file === 'wiki/log.md')) {
    points.push('index/log 직접 수정이 실제 wiki 상태와 일치하는지 확인')
  }

  return points.length > 0 ? points : ['변경 범위 기준 우선 리뷰 포인트를 수동 보강할 필요가 있음']
}

function selectQuestions(categories) {
  const selected = [REVIEW_QUESTIONS[0]]
  if (categories.includes('publish-contract')) selected.push(REVIEW_QUESTIONS[1])
  if (categories.includes('wiki') || categories.includes('script')) selected.push(REVIEW_QUESTIONS[2])
  if (categories.includes('docs') || categories.includes('agent-surface')) selected.push(REVIEW_QUESTIONS[3])
  selected.push(REVIEW_QUESTIONS[4])
  return [...new Set(selected)].slice(0, 5)
}

function toMarkdown({ files, summary, categories, risk, verification, reviewPoints, questions }) {
  const filePreview = files.slice(0, 10).map(file => `- \`${file}\``)
  if (files.length > 10) filePreview.push(`- 외 ${files.length - 10}개 파일`)

  return [
    '## PR Summary',
    '',
    `- 요약: ${summary}`,
    `- 범주: ${categories.join(', ') || 'unclassified'}`,
    `- 위험도: ${risk}`,
    '',
    '## Changed Files',
    '',
    ...filePreview,
    '',
    '## Verification Impact',
    '',
    ...verification.map(line => `- ${line}`),
    '',
    '## Review Points',
    '',
    ...reviewPoints.map(line => `- ${line}`),
    '',
    '## Reviewer Questions',
    '',
    ...questions.map(line => `- ${line}`),
    '',
  ].join('\n')
}

function main() {
  const args = parseArgs(process.argv)
  const files = getChangedFiles(args)
  const categories = categorize(files)
  const summary = summarize(files, categories)
  const risk = inferRisk(categories)
  const verification = buildVerification(categories)
  const reviewPoints = buildReviewPoints(files, categories)
  const questions = selectQuestions(categories)
  const markdown = toMarkdown({ files, summary, categories, risk, verification, reviewPoints, questions })

  if (args.output) {
    fs.writeFileSync(args.output, markdown)
  } else {
    process.stdout.write(markdown)
  }
}

main()
