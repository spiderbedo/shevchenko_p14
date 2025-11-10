chet = 0
nechet = 0
lol = input(" ")
numb = list(map(int, lol.split()))
for i in numb:
    if i % 2 == 0:
        chet += i
    else:
        nechet += i
print("Сумма четных:", chet, "Сумма нечетных:", nechet)
