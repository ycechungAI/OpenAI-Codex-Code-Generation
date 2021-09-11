import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def get_score(name, score):
    return (name, score)

def get_winner(scores):
    max_score = max(scores, key=lambda x: x[1])
    max_score_count = len([score for score in scores if score[1] == max_score[1]])
    if max_score_count > 1:
        return -1
    return max_score[0]

def main
    n = int(input())
    scores = []
    for i in range(n):
        name, score = input().split()
        score = int(score)
        scores.append(get_score(name, score))
    print(get_winner(scores))

if __name__ == "__main__":
    main()
