number_of_problems = int(input())
count = 0
for i in range(0, number_of_problems):
    surety = input()
    surety_list = surety.split(" ")
    if surety_list.count('1') >= 2:
        count += 1
print(count)
