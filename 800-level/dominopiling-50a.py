import math


def solution(board_dimensions):
    total_squares = int(board_dimensions[0]) * int(board_dimensions[1])
    print(math.floor(total_squares / 2))


board_dimensions = input().split(" ")
solution(board_dimensions)
