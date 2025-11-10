text_lines = []
while True:
    line = input()
    if line == "":
        break
    text_lines.append(line)

text = " ".join(text_lines).lower()
for i in ",.!?;:-":
    text = text.replace(i, "")

words = text.split()
counts = {}
order = []

for word in words:
    if word not in counts:
        counts[word] = 1
        order.append(word)
    else:
        counts[word] += 1

for i in range(len(order) - 1):
    for j in range(i + 1, len(order)):
        if counts[order[j]] > counts[order[i]]:
            order[i], order[j] = order[j], order[i]

for w in order:
    print(w)
