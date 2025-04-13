##5 вариант
with open(r"IN 1.txt", "r") as file:
    s = file.readline().strip()
    t = file.readline().strip()
for i in range(len(s) - len(t) + 1):
    if s[i:i + len(t)] == t:
         print(i + 1, end=" ")