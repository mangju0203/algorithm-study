"""
문제: 전화번호 목록

문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.


링크: https://school.programmers.co.kr/learn/courses/30/lessons/42577

1. .startswith()를 이용해서 접두어인지 확인! 
startswith()는 문자열이 특정 문자열로 시작하는지 확인하는 메서드입니다. 
A.startswith(B)라고 하면, A가 B로 시작하면 True, 아니면 False를 반환합니다.

2. 문자열을 .sort()로 정렬하면, 접두어인 경우에는 반드시 인접하게 위치하게 됨. 자릿수대로 비교해서 정렬하기 떄문

3. for 문으로 인접한 것만 비교하면됨. 뒤의 원소가 접두어라면 바로 옆에 있을 테니!!
"""

"""
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        answer = phone_book[i+1].startswith(phone_book[i])
        if answer == True:
            break
    if answer == True:
        answer = False
    else:
        answer = True
    return answer
"""

"""
다른 사람 풀이: 해시맵 이용
- HashMap은 이름표(key) -> 값(vlaue) 구조로 데이터를 저장하는 구조
- python 에서는 딕셔너리 dict 가 해시맵 역할을 함
- 전화번호를 해시맵에 저장해두고 "1" -> "11" -> "119" 이런식으로 접두어가 있는지 확인   
- 모든 전화번호를 먼저 저장해두고, 각 전화번호의 앞부분을 하나씩 잘라보며 실제 번호로 존재하는지 확인 ]
- temp = "" 에서 temp에 하나씩 문자를 더해가며, temp가 해시맵에 존재하는지 확인
"""

def solution(phone_book):
    answer = True

    # 전화번호들을 저장할 빈 딕셔너리(해시 맵)을 만든다
    hash_map ={}

    # 전화번호를 해시맵에 저장
    for phone_number in phone_book:
        # 전화번호를 key로 해서 해시맵에 저장한다
        # 여기서 value인 1은 특별한 의미가 없다
        # 우리는 저노하번호가 존재하는지만 확인할 것 
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # temp 가 해시맵에 존재하거나 phone_number 에 존재하지 않은면  false
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
