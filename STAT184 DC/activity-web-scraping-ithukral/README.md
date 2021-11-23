# Activity: Scraping Nuclear Reactors

## Instructions 

- Create a new R Notebook in this repo and add content similar to templates provided for other activities (you may also want to refer to the Style Guide Appendix in DataComputing eBook)
- Complete the Scraping Nuclear Reactors Activity found in the DataComputing eBook
    - Make sure you carefully follow the instructions and mirror the code in the activity as you work 
    - **Every task in the activity should have narrative text describing your observations; most steps also require code chunks and corresponding output**
    - You should make commits in GitHub as you complete the activity
- Submit a completed R Notebook to Canvas before the deadline


## Tips & Errors in Book

- Wikipedia is a dynamic resource, and may have changed slightly since the activity was written
- **Your Turn**: Reconstruct Info-Graphic of Japan Reactors
    - Tip: It's fine to use `mutate(status_change = !is.na(status))` to plot a generic marker to indicate "status change" rather than points with different shapes for each possible status
    - Tip: If you want to create a new name to indicate both the reactor and its number, the `paste()` function will be helpful
    - Tip: You can adjust the figure dimensions in the code chunk options (click on the gear icon within the code chunk)


## Grading

Assignment is worth a total of 15 points.

- [3 points] Successfully scrape raw data for Japan Reactors from Wikipedia
- [3 points] Your Turn: Tidy Data & Data Cleaning (Japan)
- [3 points] Your Turn: Plot Net Generation Capacity vs Construction Date
- [3 points] Your Turn: Scrape & Clean China Data (then merge with Japan)
- [3 points] Your Turn: Reconstruct Info Graphic of Japan Reactors (or other country of interest)


