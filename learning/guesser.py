import random


answers1 = [
'a','a','b','c','b','b','a','b','b','a',
'b','a','d','c','a','a','b','b','a','d',
'c','a','d','c','b','b','c','d','a','a',
'b','d','c','c','b','b','c','c','d','c',
'b','b','a','b','b','c','b','c','b','a',
'b','a','c','d','c','b','b','a','d','c',
'b','a','c','d','c','b','c','a','b','c',
'c','b','c','b','a'
]

answers2 = [
'b','a','a','a','c','a','d','b','b','a',
'a','b','c','b','c','a','a','a','b','c',
'd','d','c','d','b','c','b','b','d','a',
'd','b','d','a','b','b','c','a','b','a',
'd','d','b','b','c','c','a','b','a','c',
'a','a','b','b','a','c','b','a','b','c',
'b','c','c','a','a','b','d','c','c','a',
'b','a','d','a','b'
]

solved = set(random.sample(range(len(answers2)), 35))

# remaining questions (35)
remaining = [answers2[i] for i in range(len(answers1)) if i not in solved]

score = 140
j_score = 0
for i in remaining:

# for i in answers1:
	choice = random.choice('abcd')
	if choice == i:
		j_score +=4
	else:
		j_score -= 1

print(score+j_score, j_score)


