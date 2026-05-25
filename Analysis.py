import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("player_stats.csv")

print("\n===== SPORTS PERFORMANCE ANALYTICS =====\n")
print(data)

# Create Performance Score
data["PerformanceScore"] = (
    data["Runs"] * 0.25 +
    data["Goals"] * 15 +
    data["Assists"] * 10 +
    data["WinPercentage"] * 2 +
    data["AverageRating"] * 20
)

# Sort Rankings
rankings = data.sort_values(by="PerformanceScore", ascending=False)

print("\n===== PLAYER RANKINGS =====\n")
print(rankings[["Player", "PerformanceScore"]])

# Top 5 Players
top_players = rankings.head(5)

# Graph 1 - Performance Score
plt.figure(figsize=(10,5))
plt.bar(top_players["Player"], top_players["PerformanceScore"])
plt.title("Top Player Performance Scores")
plt.xlabel("Players")
plt.ylabel("Performance Score")
plt.xticks(rotation=15)
plt.show()

# Graph 2 - Win Percentage
plt.figure(figsize=(10,5))
plt.plot(data["Player"], data["WinPercentage"], marker='o')
plt.title("Win Percentage Comparison")
plt.xlabel("Players")
plt.ylabel("Win Percentage")
plt.xticks(rotation=20)
plt.grid(True)
plt.show()

# Team Analysis
team_analysis = data.groupby("Team")["PerformanceScore"].mean()

print("\n===== TEAM PERFORMANCE ANALYSIS =====\n")
print(team_analysis)

# Graph 3 - Team Performance
plt.figure(figsize=(10,5))
team_analysis.plot(kind='bar')
plt.title("Average Team Performance")
plt.xlabel("Teams")
plt.ylabel("Average Performance Score")
plt.xticks(rotation=20)
plt.show()

print("\nAnalytics Completed Successfully")
