"""
문제: n번째 원소부터 출력
정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.



링크: https://school.programmers.co.kr/learn/courses/30/lessons/181945

막혔던 부분
1. 리스트에서 n번째 원소부터 출력하는 코드를 까먹음!!
2. 그리고 리스트에서는 0번부터 시작한다는 걸 까먹음
"""
def solution(num_list, n):
    answer = []
    answer = num_list[n-1:]
    return answer