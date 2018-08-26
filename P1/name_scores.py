names = open("names.txt","r").read().replace('"','').split(",")

scores = []


for i in range(len(names)):
    summ = sum([ord(char) - 64 for char in names[i]])
    scores.append(summ*(i+1))

print("total score is",sum(scores))
