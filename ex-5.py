i = 0
lol = input(" ")
numb = list(map(int, lol.split()))
for j in range(len(numb)):
    i += numb[j]
print(i/len(numb))
