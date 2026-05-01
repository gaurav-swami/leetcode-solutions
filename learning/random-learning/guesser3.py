import random
import statistics

results = []
j_scores = []


for _ in range(100000):

    patterns = [

(['b']*25 + ['a']*23 + ['c']*17 + ['d']*10),

(['b']*24 + ['a']*25 + ['c']*16 + ['d']*10),

(['b']*26 + ['a']*23 + ['c']*17 + ['d']*9),

(['b']*23 + ['a']*24 + ['c']*18 + ['d']*10),

(['b']*25 + ['a']*24 + ['c']*17 + ['d']*9),

(['b']*24 + ['a']*23 + ['c']*18 + ['d']*10),

(['b']*26 + ['a']*22 + ['c']*18 + ['d']*9),

(['b']*23 + ['a']*26 + ['c']*16 + ['d']*10),

(['b']*25 + ['a']*23 + ['c']*16 + ['d']*11),

(['b']*24 + ['a']*24 + ['c']*17 + ['d']*10)

]
    answers = random.choice(patterns)
    random.shuffle(answers)

    score = 35 * 4
    j_score = 0

    for i in range(35):
        guess = random.choice('abc')
        if guess == answers[i]:
            j_score += 4
        else:
            j_score -= 1

    results.append(score + j_score)
    j_scores.append(j_score)


under_0 = sum(1 for j in j_scores if j > -1)
positive_j_score = (under_0/100000)*100

print("average:", sum(results) / len(results))
print("median:", statistics.median(results))
print("mode:", statistics.mode(results))
print("max:", max(results))
print("min:", min(results))
print("net positive result % out of guessing : ",positive_j_score , "%")