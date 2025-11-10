a = []
b = []
for i in range(10):
    a.append(int(input()))
for j in range(8):
    b.append(a[j] + a[j + 1] + a[j + 2])
print(b)
