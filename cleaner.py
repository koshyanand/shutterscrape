
from os import listdir, remove
file_dir = "data/"
files = listdir(file_dir)

f = open("block.txt", "r")
blacklisted = set(f.read().split())

print(len(files))

for f in files:
    words = f.split("-")
    # print(words)
    for i in range(len(words) - 2):
        if words[i] in blacklisted:
            remove(file_dir + f)
            break

files = listdir(file_dir)
print(len(files))