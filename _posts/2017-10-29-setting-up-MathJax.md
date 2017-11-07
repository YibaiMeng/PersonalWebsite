---
layout: post
title:  "Setting Up MathJax in a Jekyll Blog"
date:   2017-10-29 23:14:00 +0800
---

*I'm greatly aided by [Soham Bhattacharyya's answer][answer] on `stack overflow`. Thanks a lot!*

It would be a great convenience to use be able to use LaTex in my blog. After all, I'm writing a technical blog, so I certainly need someway to show math equations. Actually, `html` has some way of showing math symbols and equations: `MathML`, or Math Markup Language. It is absolutely lousy, and has very limited support among browsers. Even Chrome doesn't support it! So we turn to a not so native way---by using JavaScript to render the symbols. 

There exist a library for showing math symbols. All you need to do is write LaTex and the script would do the rendering for you. It's called [MathJax][mathjax], a 60 KiB JavaScript script that does all the dirty work. I'll show you how to integrate it in Jekyll.  

There are numerous guides avaliable on how to integrate MathJax into Jekyll. But many of the guides are either unclear, conflicting or obsolete. So after some experimentation, I'll show you a way that's guarenteed to work.

First, check what markdown editor you are using. Check the `_config.yml` file in the root directory of your blog. If the setting for `markdown` is set to `kramdown`, then bingo! Kramdown offers built-in support. Add the line `mathjax: true` after that `markdown: krandown` line.

Then add this code snippet just before the `head` tag. To do so, go to the `head.html` file in the `_includes` directory. Note its HEAD, not HEADER. Head is for the contents inside the `<head>` element in the html document, the place where you put all the scripts and metadatum, while "header" is for the uppermost part of the page. Add this line:
```javascript
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```
The `TeX-AMS-MML_HTMLorMML` is for, quoting the [MathJax document][doc]:
> which loads MathJax with a configuration file that includes everything you need in order to enter mathematics in either TeX, LaTeX, or MathML notation, and produces output using MathML if MathML if the browser supports that well enough, or HTML-with-CSS otherwise.
You could try other configrations.

And it's done! (Note that when running a local Jekyll server, the `_config.yml` file would not be automatically incoperated into the final build when it's changed. So restart the server to see the result.) To render the equations, write LaTex as you usually would. For inline, use `\( ... \)`. As for block, use `\[ ... \]`. Actually, the slashes `\` would need escaping, so what you'd acutally type is `\\( blahblahblah \\)` and `\\[ blublublu\\]`, respectively.

Examples:
inline: \\( 1/x^{2} \\)
and block:
\\[
\frac{1}{n^{2}}
\\]

[answer]: https://stackoverflow.com/questions/10987992/using-mathjax-with-jekyll/46349188#46349188
[mathjax]:https://www.mathjax.org/
[doc]: http://docs.mathjax.org/en/latest/configuration.html
