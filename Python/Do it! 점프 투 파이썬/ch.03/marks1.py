marks = [90, 25, 67, 45, 80]    # 학생들의 시험 점수 리스트

number = 0                      # 학생들에게 붙여 줄 번호
for mark in marks:              # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number + 1
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")
