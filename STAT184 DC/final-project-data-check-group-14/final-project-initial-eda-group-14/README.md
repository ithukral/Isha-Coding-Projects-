# Final Project: Initial Exploratory Data Analysis (EDA)

## Purpose: 

Identify at least one quality data source for your final project, load into your R environment, show some basic information about the data to get preliminary feedback.  



## Instructions 

Create an R Notebook that demonstrates the following related to your final project:  
  
- **Guiding Question (i.e., Research Question)**: Make a clear statement of a **single** guiding/research question that will drive your analysis. It should be phrased as a question that you will try to investigate (i.e., it should have a question mark) 
- (at least) TWO data sources are required:
    - *Primary data source*: This is the main data source to be used in your investigation and it MUST NOT be loaded directly from an R package (although API's are fine). You should have many cases (e.g., at least hundreds--preferably many thousands), many variables including a mixture of both categorical & quantitative variables.
    - *Other data source(s)*: No problem for these to come from an R package. 
    - Each data source must be accessible from your provided GitHub Repo (either save/push a CSV to the Repo, accessed directly from an Rmd code chunk, etc)
- For each data source please do a careful **Exploratory Data Analysis (EDA)**: 
    - Examine the data source:
        - origin and purpose (who/what/when/where/why/how data were collected)
        - key variables (types, coding, missingness, summary statistics/plots) 
    - Discover features that may influence modeling decisions:
        - investigate potential outliers
        - consideration for transforming, mutating, or recoding variables (e.g., log transformations, numeric variable that's functionally dichotomous, new variables to be calculated)
        - note inherent relationships among rows (e.g., autocorrelation, hierarchy, spatial/temporal proximity)
        - *note:* really, you're just required to look for these sort of things.  If you look and decide no action is needed, just explain your process.
    - Address research question
        - build intuition for your research question(s) as initially stated
        - note observations that prompt you to refine your research questions or add new questions to investigate


## Submit

- [**Required**] Submit your completed R Notebook to Canvas before deadline.  


## Grading

- [4 pts]: Guiding Question / Research Question stated clearly (*with a question mark*)
- [4 pts]: Examine the data (both sources)
- [4 pts]: Discover/Explore features that may influence modeling decisions (both sources)
- [4 pts]: Address research question based on observations from your data sources
- [4 pts]: Each data source must be included in the provided GitHub Repo & properly accessed in the Rmd (e.g., `read_csv()` or other means)
- Do NOT print out more than 50 rows of data in the document at any point. (e.g., each semester someone prints thousands of rows of raw data in the document and turns it in...)  [4 point penalty]


## Tips

- GitHub will not allow any single file larger than 100 MB in the repo
    - this will not be a problem at all for most projects
    - if it's close, you might try compressing the data.  It's pretty easy, Google it or visit office hours.
    - (optional) if the compressed file is still too big, you might try see if you can configure Git LFS (Large File Storage) <https://git-lfs.github.com/>
    - you can also just use a subset of the data if you have a problem with file size--ideally, by dropping variables you were not planning to use anyway, but you can also subset the rows if you must.
- It's okay if your EDA just shows lots of different things you tried & explored at this stage.  It should still be easy to understand what you did (and why), but don't necessarily worry about editing things out or making them look especially pretty (you'll do that for the Final Project Report). Just please don't print large quantities of data in the document.


