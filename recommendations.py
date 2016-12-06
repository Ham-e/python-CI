#-*- coding: utf-8 -*-

from math import sqrt

critics={
    "Lisa Rose": {"Lady in the Water":2.5, "Snakes on a Plane":3.5, "Just My Luck":3.0, "Superman Returns":3.5, "You, Me and Dupree":2.5, "The Night Listener":3.0},
    "Gene Seymour": {"Lady in the Water":3.0, "Snakes on a Plane":3.5, "Just My Luck":1.5, "Superman Returns":5.0, "You, Me and Dupree":3.5, "The Night Listener":3.0},
    "Michael Phillips": {"Lady in the Water":2.5, "Snakes on a Plane":3.0, "Superman Returns":3.5, "The Night Listener":4.0},
    "Claudia Puig": {"Snakes on a Plane":3.5, "Just My Luck":3.0, "Superman Returns":4.0, "You, Me and Dupree":2.5, "The Night Listener":4.5},
    "Mick LaSalle": {"Lady in the Water":3.0, "Snakes on a Plane":4.0, "Just My Luck":2.0, "Superman Returns":3.0, "You, Me and Dupree":2.0, "The Night Listener":3.0},
    "Jack Matthews": {"Lady in the Water":3.0, "Snakes on a Plane":4.0, "Superman Returns":5.0, "You, Me and Dupree":3.5, "The Night Listener":3.0},
    "Toby": {"Snakes on a Plane":4.5, "Superman Returns":4.0, "You, Me and Dupree":1.0}
}

# person1 과 person2 의 거리 기반 유사도 점수를 리턴
def sim_distance(prefs, person1, person2):
    # 공통 항목 목록 추출
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # 공통 평가 항목이 없는 경우 0 리턴
    if len(si) == 0: return 0

    # 모든 차이 값의 제곱을 더함
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])

    return 1/(1 + sqrt(sum_of_squares))

# p1 와 p2 에 대한 피어슨 상관계수를 리턴
def sim_pearson(prefs, p1, p2):
    # 같이 평가한 항목들의 목록을 구함
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    # 요소들의 개수를 구함
    n = len(si)

    # 공통 요소가 없으면 0 리턴
    if n == 0: return 0

    # 모든 선호도를 합산함
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # 제곱의 합을 계산
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # 곱의 합을 계산
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # 피어슨 점수 계산
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r

# 선호도 딕셔너리에서 최적의 상대편들을 구함
# 결과 개수와 유사도 함수는 옵션 사항임
def topMatches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

    # 최고점이 상단에 오도록 목록을 정렬
    scores.sort()
    scores.reverse()
    return scores[0:n]
