"""
문제: 더 맵게

매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

링크: https://school.programmers.co.kr/learn/courses/30/lessons/42626

문제 풀이 접근
1. 
def solution(scoville, K):
    answer = 0
    scoville.sort()  
    while scoville[0] < K:
        answer += 1
        new = scoville[0] +  (scoville[1]*2)
        del scoville[0:2]
        scoville[0] = new
        scoville.sort()
    return answer
-> 시간초과됨. 정렬을 반복문 마다 진행해서 그런듰, 흠 그러면.. min을 써보자
-> 근데 두번째로 작은 수는 어떻게 구하지??



몰랏던 부분
1. 리스트를 정렬하려면 sorted()를 사용해야함
2. 리스트명.sort()는 정렬은 해주지만,반환은 None
3. heapq 는 최솟값을 빠르게 꺼내는 자료구조 -> 이걸 몰랐음
4. 리스트를 힙으로 바꾸려면 heapq.heapify(리스트명)
6.
heapq.heapify(list)	리스트를 힙 구조로 만들기
heapq.heappop(list)	가장 작은 값 꺼내기
heapq.heappush(list, x)	값 x 넣기
"""

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1 and scoville[0] < K:
        answer += 1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+min2*2)
    if scoville[0] < K:
        answer = -1
    return answer