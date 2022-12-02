with open('input.txt', 'r') as file:
    data = file.read()
file.close()

data = data.split('\n')

rounds = []

for x in data:
    tempData = x.split(' ')
    rounds.append(tempData)
    print(tempData)

# Outcome Score
win = 6
draw = 3
lose = 0

# Outcomes
# A X = Rock
# B Y = Paper
# C Z =  Scissors

scores = {'A' : 1, 'B' : 2, 'C' : 3}
subs = {'X' : 'A', 'Y' : 'B', 'Z' : 'C'}

rps_win={'A':'C','B':'A','C':'B'}
rps_lose={'A':'B','B':'C','C':'A'}

# A beats C, B beats A, C beats B
# X > Z         Y > X   Z > Y
# A = 1, B = 2, C = 3
# Convert all X,Y,Z into A,B,C?


# Part 1
score = 0
for x in rounds:
    if rps_win[x[0]] == subs[x[1]]:
        score += (lose + scores[subs[x[1]]])
        print('Round Score : ', lose +scores[subs[x[1]]])
        print("Player Loses: ", score)
    elif rps_lose[x[0]] == subs[x[1]]:
        score += (win + scores[subs[x[1]]])
        print('Round Score : ', win + scores[subs[x[1]]])
        print("Player Wins: ", score)
    else:
        score += (draw + scores[subs[x[1]]])
        print('Round Score : ', draw + scores[subs[x[1]]])
        print("Draw: ", score)


print("----------------------------------")
# Part 2:

# Y = Draw
# X = Lose
# Z = Win
score = 0
for x in rounds:
    print("Round", x)
    if x[1] == 'Y':
        # Draw
        score += (draw + scores[x[0]])
        print("Draw:", draw, scores[x[0]])
    elif x[1] == 'X':
        # Lose
        chose = rps_win[x[0]]
        print("Chose: ", chose)
        score += (lose + scores[chose])
        print("Lose:", lose, scores[chose])
    else:
        # Win
        chose = rps_lose[x[0]]
        print("Chose: ", chose)
        score += (win + scores[chose])
        print("Win:", win, scores[chose])
    print("Round Score: ", score)
        
print(score)
        
        




