def solution():
    players = input()
    prev_player = players[0]
    count = 1
    for player in players[1:]:
        if player == prev_player:
            count +=1
        else:
            count = 1
        if count == 7:
            print("YES")
            return
        prev_player = player
    print("NO")

solution()