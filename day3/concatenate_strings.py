"""
문제: 문자열 붙여쓰기
두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181946

"""
str1, str2 = input().strip().split(' ')
print(str1+str2)

