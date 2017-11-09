---
layout: post
title:  "Green Function Method, and reciporcity"
date:   2017-10-12 20:13:46 +0800
---
We know that the core of electrostatic problems is Possion's equation:

\\[
\nabla^2V(\vec{x})=-\frac{\rho(\vec{x})}{\epsilon_0}
\\]

Solving the special case where $$\rho=0$$ ,that is, the Laplace equation, is easier(not *easy*, just a tiny bit easier). There's a variety of method avaiable, for example separation of variables. Also, due to numerous properties of the Laplace equation, solving it numerical is also easier. However, for most practical problems, there's bound to be some charges. So what can we do?

Well, not all boundary problems are *that* diffcult to solve! Boundary problems that only include point charges are (a tiny bit) easier. For example, there's the method of images that we could make use of. So, could we utilize the results of point charge problem and apply them to general situations? The answer is an absolute yes!

## Dirac's delta function
To describe the charge density of point charges, we invent the Dirac delta *function*:
$$
\delta(x) = 0
$$
when $$x \ne 0$$, and
$$
\delta(x) = \infty
$$
when $$x = 0$$.

Note that this is not a literal function. It's actually a distribution, a limit of functions. For example, the standard normal distribution
$$
\frac{1}{2\pi\sqrt{\sigma}} e^{-\frac{x^2}{2\sigma^2}}
$$
will *become* the delta function when $$\sigma$$ approches zero. The rigorous defination of the delta function is done in this way.

A point charge occupies infitismal space, yet carries a finite amount of charge.  So while the delta function is infinite at zero, it's integral is not. That is,
$$
\int{\delta(x)dx} = 1
$$
for *any* interval which contains zero, and
$$
\int{\delta(x)dx} = 0
$$
for all the intervals without. The "one" there is chosen to keep things simple. Any finite number will do. In fact, one should think of the delta function as a *symbol* that can only be used under the integral. For example, one of delta function's most important property:
$$
\int{f(x)\delta(x)dx} = f(0)
$$
where $$f$$ is some ordinary function. Only the value of $$f$$ at zero matters. Everything else is swept "under the rug". It is best to think of the delta function as something waiting to be integrated.

Of course, is easy to generalize  the function to more dimensions. Simply have the integral integrate over *volume*, instead of length. Also, its easy to change the point where the value is infinte. For example, $$\delta(x-3)$$ is infinite at $$x=3$$, and critical point here is three.

So now we can describe a point charges' density using the delta function. A point charge $$q$$ at $$\vec{x}'$$  could be represented as
$$
\rho(\vec{x}) = q\delta(\vec{x} - \vec{x}')
$$
note the delta function here is its three dimensional generalization.

## Green Function

Now we are ready to tackle the real challenge.  The potential a point charge at $$x'$$ causes satisfies Possions equation:
$$
\nabla^2V(\vec{x}) = -\frac{q}{\epsilon_0}\delta(\vec{x} - \vec{x}')
$$




##

Edited!

To add new posts, simply add a file in the `_posts` directory that follows the convention `YYYY-MM-DD-name-of-post.ext` and includes the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}


{% endhighlight %}
$$ \frac{go}{to^hell} $$
\\[
|\psi_1\rangle = a|0\rangle + b|1\rangle
\\]

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: http://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
