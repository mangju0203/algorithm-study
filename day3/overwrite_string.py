"""
문제: 문자열 겹쳐쓰기
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 
문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181943

my_string	overwrite_string	s	result
"He11oWor1d"	"lloWorl"	2	"HelloWorld"
"Program29b8UYP"	"merS123"	7	"ProgrammerS123"

발생한 에러
1. TypeError: 'str' object does not support item assignment 
-> Python의 문자열은 수정 불가능한 자요령(immutable)

막혔던 부분: 
1. 문자열을 합하는 부분을 까먹어서 + 연산자를 쓰지 않았음.. 그냥 대입하려고 했음
2. overwrite_string 의 문자열을 붙이고 남은 my_string 값을 이어서 출력하는 부분에서 고민함 

"""

def solution(my_string, overwite_string, s):
    print(len(overwite_string))
    answers = my_string[:s] + overwite_string[:] + my_string[s+len(overwite_string):]
    print(answers)

solution("He11oWor1d","lloWorl",2 )