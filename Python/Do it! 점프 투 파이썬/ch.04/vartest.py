a = 1    # 함수 밖의 변수 a
def vartest(a):    # vartest 함수 선언
    a = a + 1

vartest(a)    # vartest 함수의 입력값으로 a를 대입
print(a)    # a 값 출력
