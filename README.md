# Berlin Population Dashboard
End-to-end development and deployment of a dashboard displaying statistics on Berlin's population between 1991 and 2019.

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python version 3.

## Project Motivation<a name="motivation"></a>

The motivation behind undertaking this project was to gain familiarity with the process of developing a dashboard of visualisations from scratch. The steps of the process were as follows:

1. Creating a file to wrangle the data using pandas and build the visualisations using Plotly
2. Writing the HTML file for the web page using a template from Bootstrap
3. Creating the instantiate file to make use of Flask to eventually deploy the files as a web app

The version of the files contained in this repository can be used to render the app on a local machine. The final web version of the app was deployed via Heroku, and can be viewed [here](https://berlin-population-dashboard.herokuapp.com/)

## File Descriptions <a name="files"></a>

- data: folder containing data sets in CSV format
- myapp: folder containing HTML file for web page, image files and instantiate & routes files
- wrangling_scripts: contains file for wrangling and visualising data

To render the dashboard locally, download and navigate to the repository and enter the command
```python myapp.py```

## Licensing, Authors, Acknowledgements <a name="licensing"></a>

The data visualised in this dashboard is publically available from the website of the [Amt fuer Statistik Berlin-Brandenburg](https://www.statistik-berlin-brandenburg.de/)
