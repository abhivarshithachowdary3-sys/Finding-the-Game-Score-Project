player_name = input("Enter the Player's Name:")
games_played = int(input("Enter the numbers of Games played by the Player:"))
total_score = int(input(f"Enter the total score after playing {games_played} games:"))

average_score = total_score / games_played

print("\nPlayer Name:",player_name)
print("Number of games played:",games_played)
print("Total Score won by the Player:", total_score)
print("Average Score of the Player:", average_score)