import random

answers = [
'a','a','b','c','b','b','a','b','b','a',
'b','a','d','c','a','a','b','b','a','d',
'c','a','d','c','b','b','c','d','a','a',
'b','d','c','c','b','b','c','c','d','c',
'b','b','a','b','b','c','b','c','b','a',
'b','a','c','d','c','b','b','a','d','c',
'b','a','c','d','c','b','c','a','b','c',
'c','b','c','b','a'
]

choices = ['a','b','c','d']

scores = []

for _ in range(100000):
    solved = set(random.sample(range(75), 35))
    score = 35 * 4

    for i in range(75):
        if i not in solved:
            guess = random.choice(choices)
            if guess == answers[i]:
                score += 4
            else:
                score -= 1

    scores.append(score)

print("avg:", sum(scores)/len(scores))
print("min:", min(scores))
print("max:", max(scores))