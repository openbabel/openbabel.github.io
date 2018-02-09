---
title: Molecular mechanics
permalink: /Molecular_mechanics/
---

Introduction
------------

In molecular mechanics, equations are used to calculate the interations and the corresponding energies. These equations follow the classical laws of physics and the atoms are represented as particles (nuclei) without considering the electrons. The atoms are connected via bonds, this means that it is not possible to simulate reactions in molecular mechanics. Bonds cannot be formed or broken (More advanced techniques such as QM/MM could be used for this).

A force field is a set of equations and parameters for these equations. A simple forcefield looks like this:

<tex>E_{tot} = E_{bond} + E_{angle} + E_{torsion} + E_{vdw} + E_{electostatic}</tex>

Each of these individual energy terms needs parameters which depend on the atom types for the interaction. See the wiki [force fields](/force_fields "wikilink") pages for more details about the functional form for each force field. The parameter files can be found in the Open Babel data/ directory.

See the [Obenergy](/Obenergy "wikilink") man page for information on how to calculate the energy for a molecule using Open Babel.

Energy minimalization
---------------------

Using a force field the energy for a given molecule can be calculated. To minimize the energy (find more stable conformation), the forces acting on each atom can be calculated by taking the negative derivative of the energy function with respect to the coordinates of the atom.

<tex>\\bf{F_a}=-\\nabla_a E_{tot}=-\\left(\\frac{\\partial E_{tot}}{\\partial x_a},\\frac{\\partial E_{tot}}{\\partial y_a},\\frac{\\partial E_{tot}}{\\partial z_a}\\right)</tex>

Once the forces on all atoms are known, taking small steps along the direction of the forces acting on them reduces the energy. If this process is repeated several times, a local minimum is reached. It is not directly possible to locate the global minimum since the forces acting on the atoms at the local minimum are zero. Other methods exist to sample the conformational space in a 'smart' way to reduce computational cost.

See the [Obminimize](/Obminimize "wikilink") man page for information on how to perform these minimizations using Open Babel.

### Line search

This algorithm is part of a bigger energy minimalization algorithm such as steepest descent or conjugate gradients. In the line search algorithm the local minimum is found be taking succesive steps along a search direction. The line search can be simplified to a one-dimentional problem. The first step size in the direction of the search direction is always the same. If the energy for the new position is lower the step is accepted and the step size is increased (stepsize \* 1.2). If the energy is higher, the step is rejected and the step size is decreased (stepsize \* 0.5). This results in a convergence towards the minimum. To speed this process up a convergence criteria is used: when the energy difference between successive is lower than 1e-7, no more steps are taken.

### Steepest descent

Steepest descent is an iterative optimization algorithm. It works by repeatably moving the atoms to the local minimum in the direction of their forces. This means that the directions of successive steps are orthogonal. As a result, the steepest descent algorithm converges rather slow in narrow valleys in the energy surface. Steepest descent is well suited for an initial minimization to relieve the molecule from large forces.

See the online resources for more information about steepest descent.

### Conjugate gradients

Conjugate gradients is an iterative optimization algorithm. It works by repeatably moving the atoms to the local minimum in the direction <tex>\\b{d_i}</tex>.

<tex>\\b{d_i} = -\\b{g_i} + \\gamma_i \\b{d_{i-1}}</tex>

<tex>\\gamma_i = \\frac{\\b{g_i} \\cdot \\b{g_i}}{\\b{d_{i-1}} \\cdot \\b{d_{i-1}}}</tex>

Here <tex>\\b{g_i}</tex> is the gradient for the current step, <tex>\\b{g_{i-1}}</tex> is the gradient for the previous step. Since there is no <tex>\\b{g_{i-1}}</tex> for the first step, the first step is identical to the first step for steepest descent. Conjugate gradients theoretically converges in the same number of steps as there are variables (3N, N is number of atoms). However, the linesearch never finds the real minimum (see convergence criteria) so some additional steps are needed.

See the online resources for more information about conjugate gradients.

Current implementations
-----------------------

Currently, the 2.2 development code includes three [force fields](/force_fields "wikilink"):

-   [OBForceFieldGhemical](/OBForceFieldGhemical "wikilink")
-   [OBForceFieldMMFF94](/OBForceFieldMMFF94 "wikilink")
-   [OBForceFieldUFF](/OBForceFieldUFF "wikilink")

Performance
-----------

Going from version 2.1 to 2.2, the force fields performance has increased significantly.

Here are the results for the minimization of clopidogrel (37 atoms):

OpenBabel 2.1:

    $time obminimize -c 1e-60 clopidogrel.sdf
    ...
    real    6m17.901s
    user    6m16.640s
    sys 0m0.216s

OpenBabel 2.2:

    $time obminimize -c 1e-60 clopidogrel.sdf
    ...
    real    0m4.685s
    user    0m4.616s
    sys 0m0.032s

### Compiling with SSE/AltiVec

SSE stands for streaming SIMD (single instruction multiple data) extensions. It is found in modern x86 processors. AltiVec is the same concept for PowerPC.

The instructions below apply to x86/GCC in Linux.

1. Download and extract the archive:

    $tar zxvf openbabel-2.2.tar.gz
    $cd openbabel-2.2

2. Run `configure` and specify the compiler flags:

    $./configure CXXFLAGS="-g -O2 -msse3 -mfpmath=sse"

If you are not sure what SSE version(s) your CPU supports, you can run the following command to check the CPU flags:

    $cat /proc/cpuinfo

3. Now you can run `make` and `make install`:

    $make
    $sudo make install

### OpenMP

OpenMP allows programs to run in parallel on multiple processors/cores. In the past these systems were expensive but recently dual core processors like Intel's Core2 Duo are found in affordable systems. If you bought a laptop/desktop computer in the last few months, it is very likely to have multiple cores.

To compile openbabel with OpenMP support, libgomp (GCC OpenMP (GOMP) support library) needs to be installed. Most distributions will provide this as a package.

The instructions below again apply to x86/GCC in Linux.

1. Download and extract the archive:

    $tar zxvf openbabel-2.2.tar.gz
    $cd openbabel-2.2

2. Run `configure` and specify the compiler flags:

    $./configure CXXFLAGS="-g -O2 -msse3 -mfpmath=sse -fopenmp -lgomp"

3. Now you can run `make` and `make install`:

    $make
    $sudo make install

To test the difference, we can run an optimization in a single thread or as two parallel threads by setting the environment variable OMP_NUM_THREADS.

First we set it to 1, this is the same as running obminimize without openmp:

    $export OMP_NUM_THREADS=1
    $time ./tools/obminimize -ff MMFF94 -n 1000 1CRN.mol2
    ...
    real    5m48.048s
    user    5m46.530s
    sys 0m0.368s

Next we set OMP_NUM_THREADS to 2:

    $export OMP_NUM_THREADS=2
    $time ./tools/obminimize -ff MMFF94 -n 1000 1CRN.mol2
    ...
    real    4m30.607s
    user    8m14.219s
    sys     0m1.384s

The increase in performance depends on the size of the molecule. For small molecules, using two threads is actually slower.

Online resources
----------------

-   <http://en.wikipedia.org/wiki/Molecular_mechanics>
-   <http://en.wikipedia.org/wiki/Force_field_%28chemistry%29>
-   <http://en.wikipedia.org/wiki/Steepest_descent>
-   <http://en.wikipedia.org/wiki/Conjugate_gradient>
