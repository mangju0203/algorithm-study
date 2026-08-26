"""
문제: 홀짝 구분하기
자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181944?language=python3

막혔던 부분: 
1. 입력값의 범위를 설정하는데 막혔음. 잘못된 범위의 수가 입력되면 실행을 종료하고 싶은데 continue밖에 생각이 안 났음
2. else 뒤에는 조건문을 쓰면 안되는지 몰랐음
3. print문 안에 변수의 값이 출력되게 하는 방법을 몰랐음 
"""
a = int(input())
if (a < 1 or a >1000):
    exit()
elif a % 2 == 0:
    print(a, "is even")
else:
    print(a, "is odd")