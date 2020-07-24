# Formula 1 Exploration

For this capstone project, using a Formula 1 Racing dataset from 1950-present, different aspets will be compared in regards to race sucess. 

## Background

Formula racing is a widely popular form of motosport road racing. It requires the chassis and engines of the cars to adhere to a set of specifications, but in open formula racing, a team is allowed to choose or design the chassis and/or engine to fit said specifications. 

## Dataset

The dataset came from Ergast which is a public API. There were SQL database dumps provided. This dataset contained over 13 data frames which contained the entirety of the history of Formula 1 Racing. 
http://ergast.com/mrd/db


## Questions

What makes for a successful driver? What makes for a successful constructor? Can you just buy your way the the constructors cup? 

Lewis Hamilton, who had one World Drivers' Championship (WDC) in 2008 before switching teams in 2013, to a Mercedes Constructor team that had only won only 2 WDC trophies in the 60 years prior. He has since won 5 straight WDC trophies, how did he achieve that? What changed?

## Data Analysis
The EDA on the data was performed primarily using Jupyter Notebooks. There were fatal errors that occured while using the provided SQL files. The alternative csv files were available for download which proved to be much more successful.

While analyzing what aspects of a race affect the outcomes the most, it was determined that the results.csv data table would be the most useful. Columns that were initially very useful were 'grid', 'rank', and 'positionOrder'. The table was masked to analyze the different parameters (e.g. 2nd starting position, or 4th fastest lap time) that were to be analyzed. 

![](images/Finishesbytopten.png)


## Goals

The goals are to determine what resources and factors increase or decrease the likelihood of winning a F1 race. Some of the factors to examine are pole positions, fastest laps, engine manufacturers, chassis manufacturers, and tire compositions, home country track advantage, among many others.

