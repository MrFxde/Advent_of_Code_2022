#Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
# open file 
# for every block of numebrs add them all up
# add to an array
# sort them
#return last element

file_path = "/Users/mrfxde/Desktop/Projects/Advent_of_Code/day1_input.txt"
with open(file_path) as file:
    total = 0
    arr = []
    for line in file:
        
        if line == "\n":
            #print("if", line)
            arr.append(total)
            total = 0
        else:
            #print("else", line)
            total += int(line.rstrip())

arr.sort()
#Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?
top_three = arr[-3:]
total = 0
for num in top_three:
    total += num
print(total)






