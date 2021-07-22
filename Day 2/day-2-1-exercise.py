# Example Input
# 39
# Example Output
# 12 (3+9)

num = input()
add = 0
for i in range(len(num)):
    add = add+int(num[i])
print(add)
