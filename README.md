# football-players-data-analysis-python

## Description
This dataset contains stats for 10 football players from Europe's top leagues.

## Case Study
Manchester United football club wants to know which player they should sign for the Striker position from the list provided. You need to perform a comparative Analysis between players and suggest two players whom they should sign.

**Additional Note:**
- One of the players should be less than 25 years of age
- One of the players should have preferably played in the English premier league

## Column name & description
![image](https://github.com/aditigangar-dataanalystduo/football-players-data-analysis/assets/110927056/07ccc1bb-e001-4783-9eec-e5713b1be796)

- Player Name: Name of the player
- Age: The age of the player
- Current Club: Name of the club that the player currently plays for
- Opponent: Name of the team that the player played against
- Competition: Name of the competition.
- Date: Date of the match played
- Position: Playing position of the player
- Mins: Minutes played
- Goals: Total goals
- Assists: Total assists
- Yel: Yellow card
- Red: Red card
- Shots: Total shots
- PS%: Pass success percentage
- AerialsWon: Aerial duels won
- Rating: Rating per match

## Exploratory Data Analysis
- **Check the number of players with ages less than and greater than 25 years.**
   -  **Observation:** Six players with ages less than 25 years
  
![image](https://raw.githubusercontent.com/AyishaRana/football-players-data-analysis-python/refs/heads/main/age%20count.png)

- **Check the number of players played in the English premier league.**
  - **Observation:** Three players have played in the English premier league

![image](https://raw.githubusercontent.com/AyishaRana/football-players-data-analysis-python/refs/heads/main/english%20premier%20league.png)

- **Check the total number of goals & assists scored by each player**
   - **Observation:**
      - Victor Osimhen & Harry Kane are the top 2 in goals.
      - Randal Kolo Muani is at the top for assists.
      - Six players with goal contributions of more than 20.
    
![image](https://raw.githubusercontent.com/AyishaRana/football-players-data-analysis-python/refs/heads/main/total%20contribution.png)
   
- **Check the average no. of Shots, PS%, AerialsWon & Ratings per match by each player**
   - **Observation:** Top players based on, 
      - Avg. Shots per match – Mitrovic & Osimhen
      - Avg.  PS% per match – David, Ramos, Thuram, Højlund
      - Avg.  AerialsWon per match – Mitrovic, Toney
      - Avg. Rating – Multiple players

![image](https://raw.githubusercontent.com/AyishaRana/football-players-data-analysis-python/refs/heads/main/avg%20ratings.png)

- **Check the Mean, Median & Mode Ratings per match by each player**
   - **Observation:**
      - Not much difference between the players

![image](https://raw.githubusercontent.com/AyishaRana/football-players-data-analysis-python/refs/heads/main/mean%20median%20mode.png)

- **Check Variance & Std. Deviation for each player to find the player whose ratings vary the least**
   - **Observation:**
      - If the standard deviation is high, this means that values are typically a long way from the mean. If the standard deviation is low, values tend to be close to the mean
      - **Harry Kane** & **Dusan Vlahovic** are the players which Manchester United should target. Both players satisfy the criteria.

![image](https://raw.githubusercontent.com/AyishaRana/football-players-data-analysis-python/refs/heads/main/variance%20std-dev.png)