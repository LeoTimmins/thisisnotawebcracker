file = open("data/dict.txt", "w")

for i in range(1_000_000):
    file.write(str(i) + "\n")