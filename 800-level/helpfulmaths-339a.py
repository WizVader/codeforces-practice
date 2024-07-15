def solution():
    user_input = input().split('+')
    user_input.sort()
    output = ""
    if len(user_input) == 1:
        print(user_input[0])
        return
    else:
        for i in range(len(user_input)):
            if i == len(user_input) - 1:
                output += user_input[i]
            else:
                output += user_input[i] + '+'
    print(output)

solution()