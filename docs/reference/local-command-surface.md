# Local Command Surface Reference

이 문서는 `ai-survival-log`에서 사용되는 로컬 command surface와 대표적인 workflow를 정리한 reference 문서다.

## Command Surface

### `/journals:backup`

- save the current conversation into `raw/journals/`

### `/wiki:ingest`

- ingest source material into the wiki

### `/wiki:query`

- search the wiki and answer with citations

### `/wiki:file-answer`

- turn a useful answer into a durable wiki page

### `/wiki:lint`

- validate wiki integrity

### `/wiki:publish`

- turn a published wiki page into downstream-compatible MDX output

### `/content:book-study-blog`

- connect book-study conversations to the blog lane

### `/content:blog-to-instagram`

- connect a blog post to the Instagram lane

### `/content:review-blog-draft`

- run the two-axis blog draft review before publish

## Workflow Reference

### `/wiki:ingest`

1. read source material
2. preserve external source in `raw/{type}/` when needed
3. create or update `wiki/sources/`
4. create or update entities, concepts, topics, or projects
5. add cross references
6. update `wiki/index.md`
7. add a `wiki/log.md` entry

### `/wiki:query`

1. inspect `wiki/index.md`
2. identify relevant pages
3. read raw source when necessary
4. answer with citations
5. optionally propose filing the answer into the wiki

### `/wiki:file-answer`

1. choose the right page type
2. add frontmatter
3. add cross references
4. update `wiki/index.md`
5. add a `wiki/log.md` entry

### `/wiki:lint`

Checks commonly include:

1. broken wikilinks
2. orphan pages
3. index coverage mismatch
4. missing or incomplete frontmatter
5. missing related-pages sections
6. `published: true` without `slug` or `description`
7. generated/local surface contamination

### `/wiki:publish`

1. confirm `published: true`
2. convert frontmatter for the blog artifact
3. convert or flatten wikilinks
4. remove the related-pages section
5. verify downstream image compatibility
6. emit `output/blog/YYYY-MM-DD-{slug}.mdx`
7. optionally sync to downstream site
8. add a publish record to `wiki/log.md`

## Blog Pipeline

```text
wiki/topics/example.md
  ↓ /wiki:publish
output/blog/YYYY-MM-DD-example.mdx
  ↓ downstream sync
ai-survival-log-site/content/posts/YYYY-MM-DD-example.mdx
```

## Publishing Rules

- wiki is the source of truth
- `output/blog/` and downstream `content/posts/` are derived artifacts
- rerun publish when the upstream wiki page changes
- publishable pages should be readable standalone
- images need both upstream source copies and downstream served copies
