number_of_operations = int(input())

x = 0
for i in range(0, number_of_operations):
    operation = input()
    if operation[1] == '+':
        x += 1
    else:
        x -= 1

print(x)