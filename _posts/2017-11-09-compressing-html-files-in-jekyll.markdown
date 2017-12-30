---
layout: "post"
title: "Compressing HTML files in Jekyll"
date: "2017-11-09 23:11"
category: shit
---
The HTML files Jekyll generates are standard and conforming, but one small problem remains: they have lots of whitespaces in them. It not only makes control freaks like me find it diffcult to read, but also for a little less efficent for the DOM parsers to parse as well. Also, it makes the website a little bit more data consuming. So I'll setup a plugin to automatically simplifies the files when generating them.

The plugin is called [jekyll-compress-html](http://jch.penibelst.de/). It uses Liquid, the language Jekyll uses to describe the way to generate HTML files. To set it up, all you need to do is place the Liquid file `compress.html` under the `_layouts` folder. Then add the following front matter before the `default.html` template:
```yaml
---
layout: compress
---
```
Rebuild your website and all should be in order!

A few settings are be available. Add the settings in the `_config.yml` file. The defaults settings are:
```
compress_html:
  clippings: []
  comments: []
  endings: []
  ignore:
    envs: []
  blanklines: false
  profile: false
  startings: []
```
`startings` and `endings` are for removing optional starting and ending tags. I don't wish to use it, as it would make the file XML non-conforming. Might cause a tiny bit of trouble for some browsers. `comments` is for removing HTML comments. There are no comments here at all, so I'll just leave it be. `clippings` is an array of elements around which whitespace will be removed. Use `all` will remove all which are safe to remove, which I did. Others are for debug purposes, which I left alone.
