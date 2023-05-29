y = open("D:\khder.txt", "r")
g = y.read()
d = g.splitlines()
question = []
answer = []
for i in range(0, 40, 2):
    question.append(d[i])
for i in range(1, 40, 2):
    answer.append(d[i])

score = 0
name = input("enter name")
for i in range(len(question)):
    print(question[i])
    ua = input("answer")
    if ua == answer[i]:
        score += 1
    else:
        print("error")

print(name, ":", score)

y = open("D:\kh.txt", "w")
e = [name, str(score)]
y.writelines(e)
