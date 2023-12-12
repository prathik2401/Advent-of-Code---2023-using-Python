data = open(r"C:\Users\Prathik\Advent of Code\Day 1\1st Star\input.txt","r")
linesList = []
for lines in data:
    linesList.append(lines.split())
print(linesList)
sum =0
for i in linesList:
    for word in i:
        digit = []
        for letter in word:
            if letter.isdigit():
                digit.append(letter)
        score = int(digit[0] + digit[-1])
        print("Score :",score)
        sum = sum + score
    print(sum)