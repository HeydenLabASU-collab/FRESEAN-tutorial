## Introduction

This tutorial is meant to provide hands-on experience with FREquency-SElective ANharmonic (FRESEAN) mode analysis of molecular vibratios in molecular dynamics trajectories. 

A series of Jupyter notebooks will guide through the steps of the analysis and provides comparisons to harmonic normal modes (the key argument for FRESEAN mode analysis is that it does not rely on harmonic approximations). 

Trajectory files for alanine dipeptide in the gas and solutions files are provided and the mathematical steps are explained step by step. 

In case of any questions or problems, feel free to reach out to: `mheyden1@asu.edu`

## Installation Instructions

### Setup up python kernel environment

Use either `conda` or `mamba` to set up an environment with all packages required to run the Jupyter notebooks in this tutorial. 

In your terminal, run the command:

`conda env create --file=environment.yml`

(replace `conda` by `mamba` if that is what you are using)

You should then be able to select the `fresean-tutorial` kernel, when you run the Jupyter noteooks.

In addition, we need to compile a couple of `C` support libraries. If a C-compiler such as `gcc` is installed, running a simple script should o the trick:

`ctypes/compile.sh`

## Recomended Prior Knowledge

The notebooks in this tutorial will run either way. But you will be able to learn the most with the right theoretical background.

#### Molecular Dynamics Simulations

> In this tutorial, you analyze vibrations in molecular dynamics simulations under different conditions. While you will not need to perform any molecular dynamics simulations (files are provided), you should be famililar with its basic concepts.

#### Time Correlation Functions

> The methods presented here rely heavily on time correlation functions and utilize their proeprties. They provide a critical link between molecular simulations and theories in statistical mechanics that describe dynamics, fluctuations, linear response functions, and transport properties.

#### Vibrational Density of States

> The vibrational density of states effectively describe the distribution of kinetic energy over frequencies. It can be computed directly as a Fourier transform of mass-weighted velocity time auto correlation function.

#### Harmonic Normal Modes

> Harmonic normal modes represent the standard approach to descibe vibrations in general and in molecules in particular. They involve quite subtantial approximations, which tend to fail at low frequencies. In this tutorial, we will use harmonic normal modes as a baseline model to compare the results from FRESEAN mode analysis to.

#### Linear Algebra and Fourier Transforms

>Linear algebra problems such as eigenvectors and eigenvalues of Hermitian matrices play an essential role for both harmonic normal modes and FRESEAN mode analysis. Further Fourier transforms are used to speed up the calculation of time correlation fucntions and translate between the time and frequency domain.

### Literature

- M. A. Sauer & M. Heyden, "Frequency-Selective Anharmonic Mode Analysis of Thermally Excited Vibrations in Proteins", *J. Chem. Theory Comput.* **2023**, 19, 5481-5490.

- S. Mondal, M. A. Sauer, M. Heyden, "Exploring Conformational Landscapes Along Anharmonic Low-Frequency Vibrations", *J. Phys. Chem. B* **2024**, 128, 7112-7120.

- M. A. Sauer, S. Mondal, B. Neff, S. Maiti, M. Heyden, "Fast Sampling of Protein Conformational Dynamics", `arXiv:2411.08154`
