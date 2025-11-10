sentence = input()
for i in sentence:
    if i in ",.!?;:-":
        sentence = (sentence.replace(i, ""))
print(set(sentence.split()))
