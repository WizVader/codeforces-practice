def solution(contest_details, contestant_scores):
    count = 0
    k = int(contestant_scores[int(contest_details[1]) - 1])

    for score in contestant_scores:
        if int(score) != 0 and int(score) >= k:
            count += 1
    print(count)


contest_details = input().split(" ")
contestant_scores = input().split(" ")

solution(contest_details, contestant_scores)
