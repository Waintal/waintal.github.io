---
title: Research
subtitle: A short tour of what we work on. The publication list has all the details.
---
Most of what we do lies at the border between theory and numerics. We like numerical methods that follow
closely what one would do analytically: understand which mathematical structure makes a calculation possible,
then teach the computer to do it. We also care about lowering the entry cost of new calculations, so that one can
describe a problem the way one writes it on the blackboard. Much of this ends up in open-source
[software](/projects/), developed with [Christoph Groth](https://scholar.google.com/citations?user=9ZzfbNkAAAAJ), the scientific software developer of our team, with whom I work daily.

## Tensor networks and the quantics representation {#tensor-networks}

Tensor networks were developed to describe quantum many-body wave functions. A more recent line of work,
largely coming from applied mathematics, uses them to compress *functions* of many variables. Combined with the
"quantics" representation (writing a coordinate $x$ in binary, with one tensor per bit), this lets one handle
grids with $2^{40}$ points or more, provided the function has some structure across scales. The
central tool is tensor cross interpolation (TCI), which learns such a representation from a small number of
samples of the function.

We use these ideas for rather different problems: summing Feynman diagrams, solving partial differential
equations such as the Gross-Pitaevskii equation, the Schrödinger equation in first quantization,
Lindblad dynamics of superconducting circuits, or building orbitals for quantum chemistry. Part of this work is done within the
[tensor4all](https://tensor4all.org) collaboration, in particular with [Hiroshi Shinaoka](https://shinaoka.github.io) (Saitama) and [Jan von Delft](https://www.theorie.physik.uni-muenchen.de/lsvondelft/) (LMU Munich).

<figure>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">
<img src="/img/research/gpe-t25.jpg" alt=""><img src="/img/research/gpe-t5.jpg" alt=""><img src="/img/research/gpe-t15.jpg" alt="">
</div>
<figcaption>A Bose-Einstein condensate in a trap with an eightfold symmetric modulation, at three successive times, computed on a
$2^{20}\times 2^{20}$ grid with quantics tensor trains. From <a href="https://arxiv.org/abs/2507.04262">Niedermeier <i>et al.</i>, Phys. Rev. Research 8, 023006 (2026)</a>.</figcaption>
</figure>

A few entry points:
[Learning Feynman diagrams with tensor trains](https://arxiv.org/abs/2207.06135),
[Quantics tensor cross interpolation](https://arxiv.org/abs/2303.11819),
[Learning tensor networks with tensor cross interpolation](https://arxiv.org/abs/2407.02454),
and our [lecture notes](https://arxiv.org/abs/2601.03035) *Who can compete with quantum computers?*

## What can quantum computers really do? {#quantum-computing}

A perfect quantum computer could solve problems that are out of reach of classical machines. Real devices,
however, are noisy, and whether they can beat a classical computer in practice is a subtle question. We have
been studying it by building approximate classical simulators of quantum computers, using tensor network
compression, and by looking carefully at the claims made for specific algorithms (quantum supremacy
experiments, Grover's algorithm, quantum chemistry). Much of this work was done with [Miles Stoudenmire](https://itensor.org/miles/) (Flatiron Institute)
and Thomas Ayral.

<figure>
<img src="/img/research/circuit-tn.png" alt="" style="background:#fff;padding:12px;width:70%">
<figcaption>A quantum circuit rewritten as a tensor network, the starting point of our approximate simulations. From <a href="https://arxiv.org/abs/2207.05612">Ayral <i>et al.</i>, PRX Quantum 4, 020304 (2023)</a>.</figcaption>
</figure>

A few entry points:
[What limits the simulation of quantum computers?](https://arxiv.org/abs/2002.07730),
[Opening the black box inside Grover's algorithm](https://arxiv.org/abs/2303.11317),
[Feasibility of quantum chemistry on quantum computers](https://arxiv.org/abs/2306.02620),
[The quantum house of cards](https://arxiv.org/abs/2312.17570).

## Out-of-equilibrium quantum many-body physics {#many-body}

What happens to a strongly interacting quantum system driven out of equilibrium, for instance a quantum dot
under a bias voltage? Very few such problems can be solved with controlled accuracy. With [Olivier Parcollet](https://www.simonsfoundation.org/people/olivier-parcollet/) (Flatiron Institute and CEA Saclay), our approach is to compute
the perturbative (Feynman diagram) expansion to high orders and resum it. We showed how, in real time, the diagrams of a
given order can be grouped so that their number grows exponentially instead of factorially, which made
diagrammatic quantum Monte Carlo practical for out-of-equilibrium problems
([Profumo *et al.*, Phys. Rev. B 91, 245154 (2015)](https://arxiv.org/abs/1504.02132)).
We then replaced the Monte Carlo integration by tensor network learning, the "tensor train diagrammatics",
which is largely immune to the sign problem and reaches orders as high as 30
([Núñez Fernández *et al.*, Phys. Rev. X 12, 041018 (2022)](https://arxiv.org/abs/2207.06135)).
With it we could map out the out-of-equilibrium Kondo effect and Coulomb blockade of the Anderson impurity model
with controlled accuracy ([Jeannin *et al.*, Phys. Rev. B 112, 155159 (2025)](https://arxiv.org/abs/2502.16306)).

<figure>
<img src="/img/research/kondo-diamonds.jpg" alt="" style="max-width:520px;background:#fff;padding:8px">
<figcaption>Differential conductance of a quantum dot versus bias voltage $V_b$ and dot level $\epsilon_d$: Coulomb diamonds and the
zero-bias Kondo ridge, computed with controlled accuracy. From <a href="https://arxiv.org/abs/2502.16306">Jeannin <i>et al.</i>, Phys. Rev. B 112, 155159 (2025)</a>.</figcaption>
</figure>

## Time-resolved quantum nanoelectronics {#nanoelectronics}

Experiments now manipulate electrons in quantum conductors on picosecond time scales, and concepts from
quantum optics (single-particle sources, interferometers, tomography) are getting their electronic counterparts.
We develop methods to simulate these time-dependent regimes in realistic devices, including the electrostatics,
and we work closely with experimental groups, in particular with Christopher Bäuerle's team in Grenoble.

<figure>
<img src="/img/research/mz-pulses.jpg" alt="" style="width:70%">
<figcaption>A voltage pulse travelling along the edge states of an electronic Mach-Zehnder interferometer, without (top) and with (bottom)
electron-electron interactions. From <a href="https://arxiv.org/abs/2602.23973">Kumar, Kloss and Waintal (2026)</a>.</figcaption>
</figure>

A few entry points:
[Numerical simulations of time-resolved quantum electronics](https://arxiv.org/abs/1307.6419),
[Tkwant](https://arxiv.org/abs/2009.03132),
[Electronic interferometry with ultrashort plasmonic pulses](https://arxiv.org/abs/2408.13025).

## Quantum transport

Quantum transport is where many of our tools come from. Our first code, KNIT, was based on a "knitting" algorithm
that computes Green's functions of systems of arbitrary geometry and number of terminals, with arbitrary internal degrees
of freedom (spin, superconductivity, orbitals)
([Kazymyrenko and Waintal, Phys. Rev. B 77, 115119 (2008)](https://arxiv.org/abs/0711.3413)).
It was followed by [Kwant](https://kwant-project.org), developed with [Christoph Groth](https://scholar.google.com/citations?user=9ZzfbNkAAAAJ), [Michael Wimmer](http://www.michaelwimmer.org) and [Anton Akhmerov](https://antonakhmerov.org) (TU Delft)
([Groth *et al.*, New J. Phys. 16, 063065 (2014)](https://arxiv.org/abs/1309.2926)), its time-dependent extension
Tkwant, developed with Thomas Kloss, and solvers for the self-consistent quantum-electrostatic problem. For an overview, see
[Computational quantum transport: a scattering approach perspective](https://arxiv.org/abs/2407.16257).

<figure>
<img src="/img/research/transport-knit-kwant.jpg" alt="" style="max-width:640px;background:#fff">
<figcaption>Local current in an electronic Mach-Zehnder interferometer in the quantum Hall regime, for two samples with
different disorder (1.2 million sites), computed with KNIT. From
<a href="https://arxiv.org/abs/0711.3413">Kazymyrenko and Waintal, Phys. Rev. B 77, 115119 (2008)</a>. Right: the logo of Kwant, its successor.</figcaption>
</figure>

We also enjoy applying these tools to physics problems together with other groups. With
[Mairbek Chshiev](https://irig.cea.fr/drf/irig/Lists/StaticFiles/Mairbek-Chshiev/index.html) (Spintec, Grenoble) we have
worked on spintronics and proximity effects in graphene, see e.g.
[Yang *et al.*, Phys. Rev. Lett. 110, 046603 (2013)](https://arxiv.org/abs/1211.6377).
With [Stephan Roche](https://icn2.cat/en/theoretical-and-computational-nanoscience-group/stephan-roche) (ICN2, Barcelona)
we have studied spin transport in graphene and other two-dimensional materials, see e.g.
[Vila *et al.*, Phys. Rev. Lett. 124, 196602 (2020)](https://arxiv.org/abs/1910.06194).

## Earlier work

### Spin transfer torque and spintronics

During my postdoc at Cornell, shortly after the first spin-torque experiments in Dan Ralph's group, we developed a
microscopic theory of current-induced spin torque in magnetic multilayers, combining scattering theory and random matrix
theory ([Waintal *et al.*, Phys. Rev. B 62, 12317 (2000)](https://arxiv.org/abs/cond-mat/0005251)).
Later, with my students and postdocs, we showed that this approach connects the different theories used in the field
(classical, scattering and circuit theory), work done with H. Jaffrès and A. Fert
([Rychkov *et al.*, Phys. Rev. Lett. 103, 066602 (2009)](https://arxiv.org/abs/0902.4360)), and extended the
Valet-Fert drift-diffusion theory to non-collinear magnetic textures
([Petitjean, Luc and Waintal, Phys. Rev. Lett. 109, 117204 (2012)](https://arxiv.org/abs/1206.4470)).
Other topics included current-induced distortion of domain walls, with M. Viret
([Europhys. Lett. 65, 427 (2004)](https://arxiv.org/abs/cond-mat/0301293)),
spin torque in very small magnetic nanoparticles, with O. Parcollet
([Phys. Rev. Lett. 94, 247206 (2005)](https://arxiv.org/abs/cond-mat/0411375)), and the interplay between spin torque
and superconductivity ([Phys. Rev. B 65, 054407 (2002)](https://arxiv.org/abs/cond-mat/0107258)).

### The Wigner crystal and quantum Monte Carlo

At low density, the Coulomb repulsion wins over the kinetic energy and electrons form a crystal, the Wigner crystal.
During my PhD with Jean-Louis Pichard we studied small disordered clusters and found signatures of an intermediate
phase between the Fermi glass and the Wigner crystal
([Benenti, Waintal and Pichard, Phys. Rev. Lett. 83, 1826 (1999)](https://arxiv.org/abs/cond-mat/9904096)).
Later, with Houman Falakshahi, we developed a Green's function quantum Monte Carlo code (with discretized space and
continuous time, convenient for mesoscopic and disordered systems) and studied the quantum melting of the
two-dimensional Wigner crystal, finding strong quantum fluctuations close to melting
([Falakshahi and Waintal, Phys. Rev. Lett. 94, 046801 (2005)](https://arxiv.org/abs/cond-mat/0406600);
[Waintal, Phys. Rev. B 73, 075417 (2006)](https://arxiv.org/abs/cond-mat/0509436)).
The same machinery gave a few general results, such as a counterpart of Leggett's theorem for persistent currents
([Phys. Rev. Lett. 101, 106804 (2008)](https://arxiv.org/abs/0804.1689)).

<figure>
<img src="/img/research/wigner-crystal.jpg" alt="" style="background:#fff;width:70%">
<figcaption>Quantum Monte Carlo simulation of 56 electrons near the melting of the two-dimensional Wigner crystal (=35$):
electronic density, in percent of the average density (left), and density-density correlations (right).
From <a href="https://arxiv.org/abs/cond-mat/0509436">Waintal, Phys. Rev. B 73, 075417 (2006)</a>, Fig. 9.</figcaption>
</figure>

### Metals in two dimensions?

Scaling theory predicts that a disordered two-dimensional electron gas is always insulating, yet experiments on
low-density silicon MOSFETs (Kravchenko and coworkers) showed a metallic behavior. With Geneviève Fleury we developed a
quantum Monte Carlo approach to the interplay between Anderson localization and electron-electron interactions, and
proposed a scenario for these observations
([Fleury and Waintal, Phys. Rev. Lett. 101, 226803 (2008)](https://arxiv.org/abs/0807.3433);
[Phys. Rev. B 81, 165117 (2010)](https://arxiv.org/abs/0902.3171)).
A short account in French for a general audience, written with Geneviève:
[Reflets de la physique 20, 6 (2010)](/downloads/Reflets_Fleury.pdf).

### Mesoscopic fluctuations

With Piet Brouwer at Cornell, I worked on random matrix theory applied to mesoscopic systems: fluctuations of the
$g$-tensor in small metal grains ([Phys. Rev. Lett. 85, 369 (2000)](https://arxiv.org/abs/cond-mat/0002139)), and Fano
resonances as a probe of phase coherence in quantum dots
([Phys. Rev. Lett. 86, 4636 (2001)](https://arxiv.org/abs/cond-mat/0010038)).
