# "The first column is what your opponent is going to play: 
# A for Rock - 1, B for Paper - 2, and C for Scissors - 3.
# X for Rock, Y for Paper, and Z for Scissors.
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round 
#(0 if you lost, 3 if the round was a draw, and 6 if you won).
# What would your total score be if everything goes exactly according to your strategy guide?

# You


file_path = "/Users/mrfxde/Desktop/Projects/Advent_of_Code/day_2_input.txt"
total_score = 0
count = 1


with open(file_path) as file:
    for line in file:
        line = line.rstrip()
        # if x (Rock) -> score + 1
        if line[2] == "X":
            total_score += 1
            if line[0] == "A": # rock and rock
                total_score += 3
            elif line[0] == "B": # rock and paper
                total_score += 0
            else:
                total_score += 6
        #   if a -> +3
        #   elif b -> +0
        #   else c -> +6
        elif line[2] == "Y":
            total_score += 2
            if line[0] == "A": # paper and rock
                total_score += 6
            elif line[0] == "B":
                total_score += 3 # paper and
            else:
                total_score += 0
        
        #elif  (Paper)y -> score + 2
        #   if a -> +6
        #   elif b -> +3
        #   else c -> +0
        else:
            if line[0] == "A":
                total_score += 0 # sci and rock
            elif line[0] == "B":
                total_score += 6 # sci and paper
            else:
                total_score += 3 # sci and sci
        #else (Scissors) z -> score + 3
        #   if a -> +0
        #   elif b -> +6
        #   else c -> +3
        if count > 2499:
            print("count",  count)
        count += 1
        
print(total_score)
