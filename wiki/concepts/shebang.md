---
title: "Shebang (#!)"
created: "2026-04-17"
updated: "2026-04-17"
type: concept
sources: []
tags: [shell, script, unix, interpreter, cli]
status: active
published: false
slug: ""
description: ""
---

# Shebang (`#!`)

**Shebang**은 스크립트 파일의 **첫 번째 줄**에 오는 특수 문자열로, 이 파일을 **어떤 인터프리터로 실행할지** OS에 알려준다.

## 형태

```bash
#!/path/to/interpreter
```

`#!` 두 글자가 합쳐져 "shebang" (또는 hashbang)이라고 불린다.

## 실제 예시

```bash
#!/bin/bash
echo "Hello, World!"
```

```python
#!/usr/bin/env python3
print("Hello, World!")
```

```js
#!/usr/bin/env node
console.log("Hello, World!")
```

## 동작 원리

1. OS가 파일을 실행할 때 첫 줄이 `#!`로 시작하면
2. 그 뒤에 적힌 경로의 프로그램을 인터프리터로 사용
3. 해당 인터프리터에 파일을 넘겨서 실행

```bash
# 이 두 줄은 동일한 동작
./script.py
python3 ./script.py
```

## `/usr/bin/env`를 쓰는 이유

```bash
#!/usr/bin/python3      # 절대 경로 — 환경마다 위치가 다를 수 있음
#!/usr/bin/env python3  # env가 PATH에서 python3을 찾아줌 (이식성 높음)
```

`env`를 쓰는 방식이 다양한 시스템에서 호환성이 좋아서 권장된다.

## .mjs와의 관계

[[concepts/es-module-mjs]] 파일에 shebang을 붙이면 Node.js CLI 도구를 직접 실행 가능하게 만들 수 있다.

```js
#!/usr/bin/env node
// 이 파일은 ./tool.mjs 로 바로 실행 가능
import { readFile } from 'fs/promises'
```

## 관련 페이지

- [[concepts/es-module-mjs]] — ES Module과 .mjs 파일 형식
