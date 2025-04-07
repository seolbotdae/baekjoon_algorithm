# 사과 상자의 가치는 가장 낮은 점수 p * 사과 개수 m 으로 결정됨
# 가능한 많은 사과를 팔았을 경우 얻을 수 있는 최대 이익
# 이익이 없으면 0 리턴

# 어짜피 낮은 점수가 끼어있으면 값을 못 받게 될 테니
# 정렬을 통해 최대한 낮은 점수끼리만 모이도록 하여 극한의 이익을 노려보자

def solution(k, m, score):
    # 수익이 나지 않는 경우는 score의 길이가 m 보다 작을 경우
    if len(score) < m:
        return 0
    
    s_score = sorted(score, reverse=True)
    
    result = 0
    
    for iter in range(len(score)//m):
        result += min(s_score[m * iter:m * (iter + 1)]) * m
    
    answer = result
    return answer