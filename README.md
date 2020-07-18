# League of Legends: Surrender at 10?

## Objective:
  The goal of this project is to figure out if one could make a model that can predict the winning team of a League of Legends game simply by analyzing the stats at the 10 minute mark.
  
## Results:
  After testing the results from four different ML Models (SVC, LinearSVC, Logistic Regression and Random Forest Classifier), it was determined the Logistic Regression  model predicted the outcome of a match the best with an accuracy score of ~.731 and a cross validation score of ~.717, making it better than randomly guessing by over 20%.'
  
## Code:
* **Language**: Python (3.7.6)
* **Packages**: pandas, numpy, sklearn, matplotlib, seaborn, pickle
  
## Resources:
* Data obtained from https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min
* Additional research about ward placement from https://mobalytics.gg/blog/detailed-analysis-warding-league-legends/
* Inspiration and guidance from [Ken Jee's Data Science Project From Scratch Playlist](https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t)
  
## Introduction: 
  League of Legends, by Riot Games, is the most popular Multiplayer Online Battle Arena (MOBA) in the world. The game revolves around two teams (Red and Blue) consisting of 5 champions each trying to destroy the other teams' bases to eventually destroy their nexus and win the game. Games usually run for about 20-30 minutes each, with some games lasting for an hour or more before a nexus is destroyed. Alternatively, teams can also choose to surrender before their nexus is destroyed if they feel as if there is no chance for them to win the game.

  Currently, a team can only surrender once they've past the 15 minute mark. This feature is to avoid teams surrendering too early based on a bad first few minutes. Previously the threshold for surrendering was at the 20 minute mark but it was reduced to 15 as it was found that more and more games could be decided before 20 minutes. While this change is, for the most part, justified by Riot, would it make sense to reduce the time even further if one could prove a game is pretty much decided by then? This question is what this project aims to answer for 10 minutes by utilizing Machine Learning models to predict the outcome of games based on the 10 minute stats.

## The Data:
The dataset for this problem shows stats from High Diamond/Low Master ranked games in the EUW server at the 10 minute mark, as well as which team ended up winning the game eventually. Such stats included amount of Kills/Deaths/Assists each team had, how much Gold/Experience the teams had, average level of the team, and how many Dragons and Heralds did each team conquer. 
  
## Data Cleaning:
My main focus for cleaning the data was to extract features that a user would be able to find (or calculated easily) through menus while playing a game. In order to achieve this goal, I performed the following operations on the dataset:

* Remove any column with information a user cannot find while in game (exact gold/experience of team, types of minions killed, etc.).
* Removed columns that told the same information twice (ex. blueKills is just redDeaths but with a sign change).
* Aggregate columns that have red and blue equivalents to single, difference columns (Kills, Deaths, AvgLevel, etc.)
* Change the Dragon, Herald, and First Blood columns to represent the team that achieved the goal rather than have multiple columns for each team.

## EDA:
After creating the corrplot below I delved into some of the more interesting correlations presented from it, especially considering warding and how it had a low correlation with every other aspect of the data.

<img src="/EDA Pictures/CorrPlot.png" width="650" height="400">

## Model Building:
After normalizing the continuous values of the data to better work with the model, I split the dataset into 80% train and 20% test. I decided to try out four different models and evaluate them using both accuracy and cross validation scores. I chose these evaluaion parameters as they are easier to deduce conclusions from. The models I tested were **Support Vector Classification (SVC), Linear SVC, Logistic Regression, and Random Forest Classification**. 

## Model Performance:
The Logistic Regression model performed the best out of all of the others compared. Something to note is that Linear SVC had scores just under that of the Logistic Regression. In a future exploration I will definitely keep tabs on both of these models and see if the performance changes when adding more data.
| Model               | Accuracy Score | Cross Validation Score |
|---------------------|----------------|------------------------|
| SVC                 | .7156          | .7116                  |
| Linear SVC          | .7303          | .7167                  |
| Logistic Regression | .7308          | .7174                  |
| Random Forest       | .7045          | .6885                  |
  
## Conclusion/Discussion:
  70% accuracy from the model is much better than a random 50% guess, which means that there are many games that are decided by the minute 10 of the game. While I would like to say that it would be reasonable if Riot decided to move the surrender time to 10 minutes, there isn't enough data in this set to generalize these findings to all ranks or possibly even servers. 

## Plans for the Future:
  I plan to revisit this topic again in the near future, once I obtain more experience with these kinds of projects. In the revisit, I plan on adding the following to the project:
* Create a more generalized model that keeps into account different ranks, servers, and possibly even Champions played.
* Scrape more data myself and adding more initial features, such as overall rank of the game and the server being played on.
* Productionize the model into an application where users can input data about their game to see how likely they are to eventually win.
