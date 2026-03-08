# KRAS Binding Pocket Dynamics: Assessment

## Overview
This repository contains the computational pipeline for detecting and characterizing binding pockets in the KRAS protein using Fpocket, followed by a 100 ns Molecular Dynamics (MD) simulation using GROMACS to analyze pocket stability and druggability.

## Directory Structure
* `01_protein_prep/`: Scripts and logs for fetching and cleaning the PDB structure.
* `02_fpocket_initial/`: Initial Fpocket outputs and pocket selection criteria.
* `03_gromacs_md/`: GROMACS `.mdp` configuration files (minimization, NVT, NPT, production) for the HOLO-KRAS.
* `04_gromacs_apo_md/`: GROMACS `.mdp` configuration files (minimization, NVT, NPT, production)for APO-KRAS.
* `05_analysis/`: Python scripts and Jupyter notebooks for trajectory analysis (RMSD, RMSF, SASA, and pocket volume).
* `Report.pdf/`: The final PDF report.

## Requirements
* Fpocket
* GROMACS 

* Python 3.x (pandas, scikit-learn, MDAnalysis, matplotlib, seaborn)

