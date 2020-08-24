# Data Analysis on the US video database of the Youtube Dataset

This project aims to perform some data analysis in the Youtube dataset, especially considering the US videos, to try to uderstand what a video must have in order
to be viewed and when it should go online, in order to maximize the number of views, and therefore, the profit of the publisher.

A similar procedure can be used to check data from other countries.

Results are presented in the notebook, as well as the general procedure and hypothesis.

Base on this, created also an Youtube Helper, a product that can simulate an assitant to a Youtuber in order to help him make his decisions, about the title and
tags of the video, as well as the time of publication.

The helper can be run with streamlit:

```bash
streamlit run app.py
```


### Author:

<ul>
  <li>Tales Marra</li>
</ul>

### Environement 

In order to be able to execute the following steps, you will need to create a Python 3 Environement.
This can be done by:

```bash
pip install requirements.txt
```

### Directory Structure

```
youtube_data_analysis
│   README.md 
│   requirements.txt
├── data
│   │   US_category_id.json                 <- metadata
│   │   USvideos.csv                        <- csv file with data
│   .gitignore                              <- gitignore
│   Youtube_US_videos_data_analysis.ipynb   <- data analysis notebook
|   app.py                                  <- the youtuber helper
```
