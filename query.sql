Select * from RegSea_22 Limit 25;

Select * from Playoff_22 Limit 25;

Select Player, AVG(pts), AVG(FGPer), AVG(ThreePer), AVG(eFG_Per), AVG(FT_Per), AVG(TS_Per) from RegSea_22
Group by player

Drop View if Exists "Elite Scorers"

-- Example View
-- Trying to find out which players were the most efficient given a big enough sample size of games/shots per game
Create View "Elite Scorers" as
Select Player, Sum(GamesPlayed), AVG(TS_Per)
From RegSea_22
Where GamesPlayed >=55
AND FGA>10
Group by Player
Order by AVG(TS_Per) DESC;

Select * from "Elite Scorers"

-- All Guards in Regular Season with their AVG TS% 
Drop View if Exists "Reg Guards"

Create View "Reg Guards" as
Select Player, SUM(GamesPlayed)/Count(GamesPlayed), AVG(TS_Per)
From RegSea_22
Where Pos='PG' or Pos='SG'
Group by Player;

Select * from "Reg Guards"



