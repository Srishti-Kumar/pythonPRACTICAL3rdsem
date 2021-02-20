import sys

print("Script Name:", sys.argv[0])
le = len(sys.argv)
for i in range(1, le):
    print("Word: ", i, ":", sys.argv[i])
print("Word Count:", len(sys.argv) - 1)


