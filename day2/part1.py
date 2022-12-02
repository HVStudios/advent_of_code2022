# Opponent:
# A for Rock,
# B for Paper
# C for Scissors

# You:
# X for Rock
# Y for Paper
# Z for Scissors

# Points:
# 1 for Rock
# 2 for Paper
# 3 for Scissors
# 0 if round lost
# 3 if round draw
# 6 if round won
def part1():
    file = open("input.txt", "r")
    total_points = 0
    for line in file:
        line = line.replace(" ", "")
        opponent_action = line[0]
        user_action = line[1]
        if user_action == "X":  # User: Rock
            total_points += 1
            if opponent_action == "A":  # Opponent: Rock, draw
                total_points += 3
            elif opponent_action == "C":  # Opponent: Scissors, won
                total_points += 6
        elif user_action == "Y":  # User: Paper
            total_points += 2
            if opponent_action == "A":  # Opponent: Rock, won
                total_points += 6
            elif opponent_action == "B":  # Opponent: Paper, draw
                total_points += 3
        if user_action == "Z":  # User: Scissors
            total_points += 3
            if opponent_action == "B":  # Opponent: Paper, won
                total_points += 6
            elif opponent_action == "C":  # Opponent: Scissors, draw
                total_points += 3
    print("Total points part 1: " + str(total_points))
    return total_points


# Opponent:
# A for Rock,
# B for Paper
# C for Scissors

# You:
# X for Lose (Rock)
# Y for Draw (Paper)
# Z for Win (Scissors)


# Points:
# 1 for Rock
# 2 for Paper
# 3 for Scissors

# 0 if round lost
# 3 if round draw
# 6 if round won
def part2():
    file = open("input.txt", "r")
    total_points = 0

    for line in file:
        line = line.replace(" ", "")
        opponent_action = line[0]
        user_action = line[1]

        if user_action == "X":              # User: Lose
            if opponent_action == "A":      # Opponent: Rock, You: Scissors
                total_points += 3
            elif opponent_action == "C":    # Opponent: Scissors, You: Paper
                total_points += 2
            else:                           # Opponent: Paper, You: Rock
                total_points += 1

        elif user_action == "Y":            # User: Draw
            total_points += 3
            if opponent_action == "A":      # Opponent: Rock, You: Rock
                total_points += 1
            elif opponent_action == "B":    # Opponent: Paper, You: Paper
                total_points += 2
            else:                           # Opponent: Scissors, You: Scissors
                total_points += 3

        else: # User: Win
            total_points += 6
            if opponent_action == "A":      # Opponent: Rock, You: Paper
                total_points += 2
            elif opponent_action == "B":    # Opponent: Paper, You: Scissors
                total_points += 3
            else:                           # Opponent: Scissors, You: Rock
                total_points += 1
    print("Total points part 2: " + str(total_points))
    return total_points


part1()
part2()