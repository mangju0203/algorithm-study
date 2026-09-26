"""
문제: 완주하지 못한 선수

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

링크:https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3

문제 풀이 접근
1. 배열의 원소를 하나씩 비교하기에는 시각 복잡도가 너무 커지는 거 아닌가..
 

몰랏던 부분
1. 일단 자꾸 정렬 걍 .sort()하면 되는데 까먹음 어케 정렬하지 이러고 잇음 ㅠ
2. 그리고 애초에 문제를 어떻게 접근해야할지 막막했음
3. 근데 해시를 어케 써야하는지 모르겠음
4. 완주하지 못한 사람이 원소 마지막에 있을 때 어떻게 처리해야할지 몰랐음
5. 그리고 반복문 안에서도 더이상 반복할 필요가 없을 때 break를 쓰지 못했음



발생한 오류
"""


# 내 풀이 - 챗지피티 썼지만 내 풀이 맞음 ㅎㅎ
"""
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] == completion[i] :
            continue
        elif participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer == '':
        answer = participant[-1]
            
            
    return answer
"""
# 다른 사람 풀이(해시 사용)
# 파이썬의 collections라는 모듈 사용 - Counter는 리스트 안에 각 값이 몇 번 나오는지 자동으로 세어주는 도구
"""
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

"""