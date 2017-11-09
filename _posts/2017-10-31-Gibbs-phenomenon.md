---
layout: post
title:  "the Gibbs Phenomenon"
date:   2017-10-31 23:30:00 +0800
---

Fourier transformation is awesome! One example of its awesomeness is how a arbitrary function, even one with a finite number of discontinuities, could be approximated to arbitrary precision using Fourier sum. Useful for generating square waves using harmonic oscillators. But there's a question: for signals with *jump discontinuities*, such as the aforementioned square wave, could the Fourier sum model the *jump* accurately? After all, how can you sum a bunch of smooth functions and end up with a discontinuities one? Well, the answer is yes and no. And that's what the Gibbs Phenomenon is: the imperfect representation of jumps by Fourier series.

# Gibbs Phenomenon

A Fourier sum
\\[
F_N(t)=\sum_{k=1}^{N}{C_ke^{ik\omega t}}
\\]
is used to approximate periodic function \\(F(t) \\). For the piecewise continuous parts in \\( F(t) \\), when $$N$$ gets bigger, the sum approaches the function in a uneventful way. But right after the jump, the sum will always overshoot a little bit, then oscillate for a while. The *spike* will happen, no matter how big $$N$$ gets. Or in formal words:
For a function $$F(t)$$ which has a jump at $$$x_0$$, that is,
\\[
\lim_{t \to t_0^+}{F(t)} = F_1
\\]
while
\\[
\lim_{t \to t_0^-}{F(t)} = F_1-a
\\]
the following limit exists:
\\[
\lim_{N \to +\infty}{F_N(t_0+\frac{T}{2N})} = F_1 + Wa
\\]
where $$W$$ is a number with the first few digits as
\\[
W = 0.08949\dots
\\]
Similar limits exists just before the jump.

This result is troubling: with a spike of one tenths of the original function, how can you call the Fourier series converging? Well, first, even thought the spikes will never go away, the place the spike happens is getting closer and closer to the jump point, making the spike narrower and narrower. Unlike the Dirac delta function, the height of the spike remain unchanged, so the area under the spike, or in a similar measure, the difference in power for signals, has a limit of zero. So in terms of energy, the convergence is sound.

Also, remember what the Dirichlet conditions says:
> The Fourier series is convergent where the original function is continuous

Simply *convergent*, or pointwise convergent, not *uniform convergent*! The Gibbs effect is an example of not uniform convergent. The series is uniform convergent on any domain between the two neighboring points of discontinuity, but not so on the open domain $$(t_{dis}, t_{nextDis})$$ where the two $$t$$s are the two discontinuities. Only pointwise convergence here. Also, thought the series is convergent at the jump point themselves, they converge to the average of the left and right limits at that point. So now the Gibbs effect seems not too unreasonable. Or as the Wikipedia article puts,
>There is no contradiction in the overshoot converging to a non-zero amount, but the limit of the partial sums having no overshoot.

# In a Physical Perspective
From a signal processing point of view, the Gibbs phenomenon is the step response of a low pass filter. A ideal brick-wall low pass filter actually. With the transfer function of a low pass filter being a sinc function, the overshoot and the ripples could be seen as the result of convolving the step function with the sinc function. The oscillation of the sinc is the cause of the overshoot.

To be precise, the phenomenon is a *ringing* one. Not only does the signal overshoots, it also undershoots. It's actually called a *ringing artifact*, a important problem in signal processing.
