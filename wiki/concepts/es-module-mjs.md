---
title: "ES Module과 .mjs 파일"
created: "2026-04-17"
updated: "2026-04-17"
type: concept
sources: []
tags: [javascript, es-module, commonjs, nodejs, module-system]
status: active
published: false
slug: ""
description: ""
---

# ES Module과 .mjs 파일

`.mjs`는 **ES Module (ESM)** 형식의 JavaScript 파일을 명시적으로 나타내는 확장자다.

## 배경: CommonJS vs ES Modules

JavaScript에는 두 가지 모듈 시스템이 있다.

| 구분 | CommonJS (`.cjs`) | ES Module (`.mjs`) |
|------|-------------------|---------------------|
| 확장자 | `.js`, `.cjs` | `.mjs`, `.js` |
| import 방식 | `require()` | `import` / `export` |
| 로딩 방식 | 동기(synchronous) | 비동기(asynchronous) |
| 환경 | 주로 Node.js | 브라우저 + Node.js |
| `this` (최상위) | `module.exports` | `undefined` |

## .mjs를 쓰는 이유

Node.js는 기본적으로 `.js` 파일을 **CommonJS**로 처리한다.  
`.mjs` 확장자를 쓰면 "이 파일은 ESM이다"라고 Node.js에 명시적으로 알려준다.

```js
// CommonJS (require.js)
const fs = require('fs')
module.exports = { hello }

// ES Module (hello.mjs)
import fs from 'fs'
export { hello }
```

## package.json으로 대체하는 방법

`.mjs` 대신 `package.json`에 `"type": "module"`을 설정하면 `.js` 파일도 ESM으로 처리된다.

```json
{
  "type": "module"
}
```

이 경우 반대로 CommonJS 파일은 `.cjs` 확장자를 써야 한다.

## 언제 .mjs를 쓰나?

- `"type": "module"`을 설정하지 않은 프로젝트에서 **일부 파일만 ESM**으로 만들고 싶을 때
- CommonJS 프로젝트에 ESM 파일을 **혼용**해야 할 때
- 라이브러리 배포 시 ESM 버전을 명확히 구분할 때 (보통 `dist/index.mjs` 형태)

## 실제 예시: 이중 배포 구조

```
my-package/
├── dist/
│   ├── index.cjs    ← CommonJS 버전
│   └── index.mjs    ← ESM 버전
└── package.json
```

```json
{
  "main": "./dist/index.cjs",
  "module": "./dist/index.mjs",
  "exports": {
    "require": "./dist/index.cjs",
    "import": "./dist/index.mjs"
  }
}
```

## shebang과의 관계

CLI 도구를 만들 때 `.mjs` 파일에 [[concepts/shebang]]을 붙이면 `node` 없이 바로 실행할 수 있다.

```js
#!/usr/bin/env node
import { readFile } from 'fs/promises'
```

## 관련 페이지

- [[concepts/shebang]] — 스크립트 인터프리터 지시 문자열
