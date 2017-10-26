---
layout: page
title: Regex Snippets for Web Design
permalink: /notes/webdesign-regex-snippets/
---

* Select font-family statements:

```
font-family:("|'|,|\s|#|\w|!|-)+;
```

* Select class rules:

```
.gist(\{|:|\.|"|'|,|\s|#|\w|!|-|;)+\}
```

* Select color statements:

```
[^-]color:[^(;|})]*(;|)
```

* Select comments

```
\/\*[^*]*\*\/
```

* Hexadecimal colors

```
\#([a-fA-F]|[0-9]){3, 6}
```

* Select Domains in links

```
https?:\/\/?(?:[-\w]+\.)?([-\w]+)\.\w+(?:\.\w+){0,5}[^\/,\s()"']
```

* Select full URLs

```
https?:\/\/?(?:[-\w]+\.)?([-\w]+)\.\w+(?:\.\w+){0,5}[^<'",\s(){}\[\]&*]*
```
