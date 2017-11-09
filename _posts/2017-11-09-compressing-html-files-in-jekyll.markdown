---
layout: "post"
title: "Compressing HTML files in Jekyll"
date: "2017-11-09 23:11"
---
The HTML files Jekyll generates are standard and conforming, but one small problem remains: they have lots of whitespaces in them. It not only makes control freaks like me find it diffcult to read, but also for a little less efficent for the DOM parsers to parse as well. Also, it makes the website a little bit more data consuming. So I'll setup a plugin to automatically simplifies the files when generating them.
