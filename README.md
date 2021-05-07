[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Displacement_strain_planet

Planetary crustal thickness, displacement, stress, and strain calculations in spherical harmonics.

## Description

**Displacement_strain_planet** provides several functions and example scripts for generating crustal thickness, displacement, gravity, lateral density variations, stress, and strain maps on a planet given a set of input constraints such as from observed gravity and topography data.

These functions solve the [Banerdt (1986)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/JB091iB01p00403) system of equations under different assumptions. Various improvements have been made to the model including the possibility to account for finite-amplitude correction and filtering [(Wieczorek & Phillips, 1998)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JE03136), lateral density variations at any arbitrary depth and within the surface or moho-relief [(Wieczorek et al., 2013)](https://science.sciencemag.org/content/early/2012/12/04/science.1231530?versioned=true), and density difference between the surface topography and crust [(Broquet & Wieczorek, 2019)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2019JE005959). 

We note that some of these functions rely heavily on the [pyshtools](https://shtools.github.io/SHTOOLS/) package of [Wieczorek & Meschede (2018)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018GC007529).

## Methods
`Thin_shell_matrix` Solve the [Banerdt (1986)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/JB091iB01p00403) system of equations under the mass-sheet approximation and assuming that potential internal density variations are contained within a spherical shell. The system links 8 parameters expressed in spherical harmonics: the topography, geoid at the surface, geoid at the moho depth, net acting load on the lithosphere, tangential load potential, flexure of the lithosphere, crustal thickness variations, and internal density variations. Minor corrections have been made in the geoid equations.

`Thin_shell_matrix_nmax` Solve the [Banerdt (1986)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/JB091iB01p00403) system of equations with finite-amplitude correction and accounting for the potential presence of density variations within the surface or moho reliefs.

`DownContFilter` Compute the downward minimum-amplitude or -curvature filter of [Wieczorek & Phillips (1998)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JE03136).

`corr_nmax_drho` Calculate the difference in gravitational potential exterior to relief referenced to a spherical interface (with or without laterally varying density) between the mass-sheet case and when using the finite-amplitude algorithm of [Wieczorek & Phillips (1998)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JE03136).

`SH_deriv` Compute on the fly first and second-order spherical harmonic derivatives with respect to colatitude and longitude.

`SH_deriv_store` Compute and store first and second-order spherical harmonic derivatives with respect to colatitude and longitude.

`Displacement_strains` Calculate the [Banerdt (1986)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/JB091iB01p00403) equations to determine strains from displacements with a correction to the shearing and twisting deformations.

`Principal_strain_angle` Calculate principal strains and angles.

`Plt_tecto_Mars` Plot the [Knampeyer et al. (2006)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2006JE002708) dataset of extensional and compressional tectonic features on Mars.

## Example scripts
`Run_demo` A jupyter notebook that contains example scripts to determine flexure, moho-relief, and strains on Mars under different assumptions, including Airy and Pratt isostasy, or due to the sole presence of a mantle plume.

`Mars_crust_displacement` A script that demonstrates how to calculate the moho-relief and strains on Mars, as a function of the mean planetary crustal thickness and elastic thickness. The contributions from crustal thickness variations and displacement are shown assuming an elastic thickness of the lithosphere. We make use of the infered displacement to predict the principal horizontal strains and principal angle, which are compared to compressive tectonic features mapped by [Knampeyer et al. (2006)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2006JE002708). 

## How to install and run ctplanet
If you would like to modify the source code, download the Displacement_strain_planet repository and install using pip (or pip3 depending on your installation).
```bash
    git clone https://github.com/AB-Ares/Displacement_strain_planet.git
    cd Displacement_strain_planet/
    pip install .
```
Alternatively, you can install Displacement-strain-planet via pip
```bash
    pip install Displacement-strain-planet
```

## To run the example scripts
```bash
    cd examples
    jupyter notebook Run_demo.ipynb
    python Mars_crust_displacement.py 
```

## Author
[Adrien Broquet](https://www.oca.eu/fr/adrien-broquet) (adrien.broquet@oca.eu)
