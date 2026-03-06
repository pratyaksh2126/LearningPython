#WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.

n = int(input("Enter number of students: "))

scores = []
for i in range(n):
    scores.append(int(input()))

unique_scores = list(set(scores))
unique_scores.sort()

runner_up = unique_scores[-2]

print("Runner-up score:", runner_up)