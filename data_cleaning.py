import pandas as pd

# Import Data 
df = pd.read_csv(r"C:/Users/Jacob's PC/Desktop/LeagueofLegendsWinPrediction/high_diamond_ranked_10min.csv")

'''
Objectives:
    -Remove GoldDiff/ExperienceDiff as it would be hard for a user to know the exact difference
    -Remove Minion/Monster Columns as well for the same reason as above
    -Aggregate columns that have red and blue equivalents to single, difference columns
    -Combine Dragon/Herald columns to be based on which team defeats them
    -Do the same with FirstBlood
    
'''

# Remove columns accounted for by other columns denoting difference
df_noDups = df.drop(["gameId", "blueTotalGold", "blueTotalExperience", "redTotalExperience", "redTotalGold", "redExperienceDiff",
                     "redGoldDiff", "blueGoldDiff", "blueExperienceDiff","blueEliteMonsters", "redEliteMonsters",
                           "blueTotalMinionsKilled", "redTotalMinionsKilled", "blueTotalJungleMinionsKilled",
                           "redTotalJungleMinionsKilled"], axis=1)

# Aggregate columns that have red and blue equivalents to single, difference columns

# Kills, Deaths, and Assists
# Note: There are other ways of dying besides being killed in the game so I will leave Kills and Deaths
#       as separate columns.
blueKillDiff = df["blueKills"] - df["redKills"]
blueDeathDiff = df["blueDeaths"] - df["redDeaths"]
blueAssistDiff = df["blueAssists"] - df["redAssists"]

# Wards
# Note: Since wards don't necessarily have to be destroyed for them to be removed (they have a timer for
#       how long they are active) I will leave the placed/destroyed columns separated.
blueWardPlacedDiff = df["blueWardsPlaced"] - df["redWardsPlaced"]
blueWardDestroyedDiff = df["blueWardsDestroyed"] - df["redWardsDestroyed"]

# Levels
blueAvgLvlDiff = df["blueAvgLevel"] - df["redAvgLevel"]

# Towers
blueTowerDestroyedDiff = df["blueTowersDestroyed"] - df["redTowersDestroyed"]

# CSPerMin
blueCSPerMin = df_noDups["blueCSPerMin"] - df_noDups["redCSPerMin"]

# Modify dataframe
df_diffs = df_noDups.drop(["blueKills", "redKills", "blueDeaths", "redDeaths", "blueAssists", "redAssists", 
                           "blueWardsPlaced", "redWardsPlaced", "blueWardsDestroyed", "redWardsDestroyed",
                           "blueAvgLevel", "redAvgLevel","blueTowersDestroyed", "redTowersDestroyed", "blueCSPerMin",
                           "redCSPerMin", "blueGoldPerMin", "redGoldPerMin", ], axis=1)

df_diffs["blueKillDiff"] = blueKillDiff
df_diffs["blueDeathDiff"] = blueDeathDiff
df_diffs["blueAssistsDiff"] = blueAssistDiff
df_diffs["blueWardPlacedDiff"] = blueWardPlacedDiff
df_diffs["blueWardDestroyedDiff"] = blueWardDestroyedDiff
df_diffs["blueAvgLvlDiff"] = blueAvgLvlDiff
df_diffs["blueTowerDestroyedDiff"] = blueTowerDestroyedDiff
df_diffs["blueCSPerMinDiff"] = blueCSPerMin

print(df_diffs.columns)
# Since it is only possible to obtain one Dragon/Herald in the first 10 minutes, I will aggregate Dragon/Herald columns
# From each team into columns that signify which team has the monster (1 if blue, -1 if red, 0 if neither)

def determineEliteMonsterTeam(monster, row):
    if row[f'blue{monster}s'] == 1:
        return 1
    if row[f'red{monster}s'] == 1:
        return -1
    return 0

df_diffs['dragTeam'] = df_diffs.apply(lambda row: determineEliteMonsterTeam("Dragon", row), axis=1)
df_diffs['heraldTeam'] = df_diffs.apply(lambda row: determineEliteMonsterTeam('Herald', row), axis=1)

# Same concept for first blood

def determineFirstBloodTeam(row):
    if row['blueFirstBlood'] == 1:
        return 1
    if row['redFirstBlood'] == 1:
        return -1
    return 0

df_diffs['fbTeam'] = df_diffs.apply(lambda row: determineFirstBloodTeam(row), axis=1)
                              
# Drop extraneous columns
df_output = df_diffs.drop(['blueDragons', 'redDragons','blueHeralds','redHeralds','blueFirstBlood','redFirstBlood'], axis=1)

df_output.to_csv(r"C:\Users\Jacob's PC\Desktop\LeagueofLegendsWinPrediction\cleanedData.csv", index=False)

print("Done")