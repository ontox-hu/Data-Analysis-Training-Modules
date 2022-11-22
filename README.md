# Workshop on "Applications for artificial intelligence (AI) in risk assessment" (AIRA)

This repo contains the materials for the training course "Applications for artificial intelligence (AI) in risk assessment", held on Friday 25 November 2022 in Sitges - Barcelona in Spain.

## Disclaimer and credits
The repo is an adapted fork from [The TAME Toolkit for Introductory Data Science, Chemical-Biological Analyses, Predictive Modeling, and Database Mining for Environmental Health Research](https://github.com/UNCSRP/Data-Analysis-Training-Modules). Materials were selected and adapted from this resource, with permission from the authors. The online Bookdown version of the complete TAME project can be found [here](https://uncsrp.github.io/Data-Analysis-Training-Modules/)

## Course materials
The course material, that were used for the Workshop can be found in [this bookdown project](https://rstudio-connect.hu.nl/connect/AIRA)

## Course contents

 1. Chapter 1: An introduction to R
 2. Chapter 2: An introduction to the tidymodels framwork for R
 3. Chapter 3: Example of a Read-Across approach, using classical and ChemBERT - Transformer structural embeddings
 4. Chapter 4: A machine learning example for compound classification

This repository is a `{bookdown}` project and can be rendered locally. To render the complete website following the steps below

 1. Clone the repository to your local system, either from the GUI in RStudio or running `git clone https://github.com/ontox-hu/aira` in the Terminal.

 2. Open the repo as an RStudio project

 3. Run the following R-code 
 ```
 install.packages("bookdown")
 install.packages("devtools")
 devtools::install(".")
 ```

 Mind that for `{keras}`, `{tensorflow}` and `{devtools}` system dependencies might be needed dependent on your Operating System and installed software. Please consult the links below for more information:
 
 - [`{keras}`](https://tensorflow.rstudio.com/)
 - [`{tensorflow}`](https://tensorflow.rstudio.com/)
 - [`{devtools}`](https://packagemanager.rstudio.com/client/#/repos/2/packages/devtools)
 
 4. Build the site locally by running 
 ```
 bookdown::render_book(".")
 ```

