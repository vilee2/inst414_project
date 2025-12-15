# inst414_project

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## WIC Overweight Prevalence Analysis
This project examines the prevalence of overweight status among White and Indigenous participants in the WIC (Women, Infants, and Children) program using national survey data. The goal is to explore racial disparities in overweight prevalence. The analysis compares a baseline model: a simple, unadjusted linear regression of overweight prevalence on race. The primary model in the analysis is a weighted linear regression adjusted for sample sizes. 

### Data
Source: National Survey of WIC Participants at the Food and Nutrition Service of the U.S. Department of Agriculture.
Population: White and Indigenous (American Indian/Alaska Native) WIC participants across the U.S. and territories.
Variables used: 
-Race (White, Indigenous)
-Percentage of overweight WIC toddlers
-Sample sizes for weighting
Key variables, such as age and sex, are missing from this analysis due to the dataset structure, where individual overweight percentages are calculated for each category within a variable and cannot be analyzed with other variables. Each observation in the dataset represents a WIC program site. 

### Methods
1. Data Cleaning: Filtered for White and Indigenous participants. Renamed columns to be more intuitive. Checked for missing values and dropped them as necessary. Dropped duplicates in dataset. Relabeled values to be more intuitive. Turned race into a boolean variable for easier analysis.
2. Modeling: Baseline model - unadjusted linear regression of overweight prevalence on race. Primary model - weighted linear regression adjusting for sample sizes
3. Comparison: Baseline model provides a benchmark for comparison. Primary model accounts for differing sample sizes and provides more reliable estimates.

### Findings
Baseline indicates a preliminary difference in overweight prevalence between White and Indigenous participants. Weighting by sample size in the primary model alters the estimates slightly by increasing the effect of the coefficient (Indigenous) and intercept (Overweight prevalence for White participants). 
#### Limitations
Potential confounders are not included. Sample may not be fully representative or generalizable to all children in the U.S. Temporal trends or regional variation were not considered. 

### Future Directions
Incorporate additional variables of interest. Consider longitudinal trends, if possible. Consider other modeling approaches. 

## Project Organization
Open the **VISUALIZATIONS** folder to see all visualizations produced during the analysis. 
Open the **CODE NOTEBOOKS FOR SPRINT 2 AND 3** folder to see the code notebooks for sprint 2 and sprint 3 submissions

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         final_project_mod and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── final_project_mod   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes final_project_mod a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

