---
layout: "post"
title: "消失的代码的鬼魂：Ken Thompson的编译器后门"
date: "2017-12-30 23:45"
---
众所周知，开源有一个好处：通过阅读源码，我可以知道这个软件有没有什么不可告人的勾当。找bug很难，看看软件有没有在偷偷的挖矿，这到很简单。所以说，开源软件给我们一种安全可靠的感觉。

真的是源码可见就安全吗？万一你的编译器被做了手脚呢？那我就用gcc！我自己编译行了吧！实在不行，我把gcc的代码看一遍！

其实，这样的话也是不能保证程序的安全性的（如果你真的看的懂gcc）。源码分析有意义，其基础在于源码能反映程序的行为。如果不能的话，分析源码是无法排除其安全隐患的。那你要说了，的确，编译器能做手脚。然而，我编译器的源码都看了，没问题呀。这样怎么不能保证安全呢？下面，我就要介绍一种方法，这种方法产生的编译器后面，在源码的任何地方都不会存在。

咱们先从最简单的情况开始：这是一个简单的编译器后门，如果程序里面有涉及登录的地方，就加一个后门。

```python
def compile(code):
  if (looksLikeLoginCode(code)):
    generateLoginWithBackDoor()
  else:
    compileNormally(code)
```

从编译器的源码里面，就能看出来这个后面。当然，任何人看到这则代码，一定会把写代码的人吃了。所有，这么做是不行的。那怎么做呢？

```python
def compile(code):
  if (looksLikeLoginCode(code)):
    generateLoginWithBackDoor(code)
  elif (looksLikeCompilerCode(code)):
    generateCompilerWithBackDoorDetection(code)
  else:
    compileNormally(code)
```

这个编译器高级了！不光会按后门，如果他发现自己在编译编译器的话，就会把后门检测与向编译器插入后门检测的功能编译到新的编译器中。（好绕啊！）这样，新的编译器在编译代码的时候，就会把后门塞进去了。
