# Final Project: Data Check

## Purpose: 

Identify at least one quality data source for your final project, load into your R environment, show some basic information about the data to get preliminary feedback.  

## Instructions 

Create an R Notebook that demonstrates the following for **at least one data source** that you intend to use for your final project:  
  
- **Research Question:** One sentence description of the topic you plan to investigate (i.e., research question)
- One or two sentences describing where/how YOU found the data (e.g., include URL to the source if possible)
- **Examine the data source:** 
    - report what you know (or don't know) about who/what/when/where/why/how the data were originally collected (note: this is NOT about how you found it, etc)
    - choose a few (3-4) key variables to describe (variable types, coding, missingness, summary statistics/plots) 
- Load the data set (e.g., `ProjData`) into your R environment and show each of the following data summaries:
    - `glimpse(ProjData)`
    - `head(ProjData)`
    - `tail(ProjData)`
    - `summary(ProjData)`


## Submit

- [**Required**] Submit your completed R Notebook to Canvas before deadline.  
- [*Optional*] You may additionally upload a CSV of your data or URL to the data source (please not larger than 5MB for CSV at this stage; more will just slow Canvas down--just submit a subset if your data are larger than that). 



## Tips

- note: use an informative object name in R (not `ProjData`) 
- Add your data set to the provided Repo if possible 
    - i.e., save it in the file directory where this repo is located
    - the data will be easier to read into the R environment if the CSV is in the same folder as the Rmd
- GitHub will not allow a file larger than 100 MB in the repo
    - if it's close, you might try compressing the data (pretty easy, Google it or visit office hours)
    - you can also just use a subset of the data if you have a problem with file size--ideally, by dropping variables you were not planning to use anyway, but you can also subset the rows if you must.
