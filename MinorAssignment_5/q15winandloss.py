'''
Modify a script to play 1,000,000 games of craps. Use two dictionaries, wins and losses, to track
the number of games won and lost for each roll number. Update these dictionaries as the simulation
progresses. For example, a key–value pair 4: 50217 in the wins dictionary would mean that
50,217 games were won on the 4th roll. At the end of the simulation, display:
(i) The percentage of games won.
(ii) The percentage of games lost.
(iii) The percentage of games resolved on each roll.
(iv) The cumulative percentage of games resolved up to each roll.
'''
import random

# Function to simulate a game of craps
def simulate_craps_game():
    roll_count = 0
    while True:
        roll_count += 1
        roll = random.randint(1, 6) + random.randint(1, 6)  # Sum of two dice rolls
        if roll in [7, 11]:
            return roll_count, "win"
        elif roll in [2, 3, 12]:
            return roll_count, "loss"
        else:
            point = roll
            while True:
                roll_count += 1
                roll = random.randint(1, 6) + random.randint(1, 6)
                if roll == point:
                    return roll_count, "win"
                elif roll == 7:
                    return roll_count, "loss"

# Initialize dictionaries to track wins and losses by roll number
wins = {}
losses = {}

# Simulate 1,000,000 games of craps
total_games = 1000000
for _ in range(total_games):
    roll_number, result = simulate_craps_game()
    if result == "win":
        wins[roll_number] = wins.get(roll_number, 0) + 1
    else:
        losses[roll_number] = losses.get(roll_number, 0) + 1

# Calculate percentages of wins, losses, and resolved games
total_wins = sum(wins.values())
total_losses = sum(losses.values())
total_resolved = total_wins + total_losses
percentage_wins = (total_wins / total_resolved) * 100
percentage_losses = (total_losses / total_resolved) * 100

# Display percentages of wins and losses
print(f"Percentage of wins: {percentage_wins:.1f}%")
print(f"Percentage of losses: {percentage_losses:.1f}%")

# Display percentage of wins/losses based on total number of rolls
print("\nPercentage of wins/losses based on total number of rolls:")
print("Rolls | % Resolved on this roll | Cumulative % of games resolved")
print("-------------------------------------------------------------")
cumulative_percentage = 0
for roll in range(1, max(wins.keys(), default=0) + 1):
    win_count = wins.get(roll, 0)
    loss_count = losses.get(roll, 0)
    total_rolls = win_count + loss_count
    if total_rolls > 0:
        roll_percentage = (total_rolls / total_resolved) * 100
        cumulative_percentage += roll_percentage
        print(f"{roll:5} | {roll_percentage:20.2f}% | {cumulative_percentage:25.2f}%")


''''
Percentage of wins/losses based on total number of rolls:
Rolls | % Resolved on this roll | Cumulative % of games resolved
-------------------------------------------------------------
    1 |                33.37% |                     33.37%
    2 |                18.75% |                     52.12%
    3 |                13.49% |                     65.61%
    4 |                 9.66% |                     75.27%
    5 |                 6.91% |                     82.18%
    6 |                 4.97% |                     87.15%
    7 |                 3.58% |                     90.73%
    8 |                 2.60% |                     93.32%
    9 |                 1.85% |                     95.17%
   10 |                 1.32% |                     96.49%
   11 |                 0.97% |                     97.46%
   12 |                 0.70% |                     98.16%
   13 |                 0.51% |                     98.67%
   14 |                 0.36% |                     99.03%
   15 |                 0.26% |                     99.29%
   16 |                 0.19% |                     99.48%
   17 |                 0.14% |                     99.63%
   18 |                 0.10% |                     99.73%
   19 |                 0.07% |                     99.80%
   20 |                 0.06% |                     99.86%
   21 |                 0.04% |                     99.90%
   22 |                 0.03% |                     99.93%
   23 |                 0.02% |                     99.95%
   24 |                 0.01% |                     99.96%
   25 |                 0.01% |                     99.97%
   26 |                 0.01% |                     99.98%
   27 |                 0.01% |                     99.98%
   28 |                 0.00% |                     99.99%
   29 |                 0.00% |                     99.99%
   30 |                 0.00% |                     99.99%
   31 |                 0.00% |                    100.00%
   32 |                 0.00% |                    100.00%
   33 |                 0.00% |                    100.00%
   34 |                 0.00% |                    100.00%
   35 |                 0.00% |                    100.00%
   36 |                 0.00% |                    100.00%
   37 |                 0.00% |                    100.00%
   40 |                 0.00% |                    100.00%
   41 |                 0.00% |                    100.00%
   42 |                 0.00% |                    100.00%
   44 |                 0.00% |                    100.00%
   45 |                 0.00% |                    100.00%
   46 |                 0.00% |                    100.00%
'''
