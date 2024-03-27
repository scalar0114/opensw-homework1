#성적관리 프로그램

student = [[0 for col in range(5)] for row in range(5)]
total = [0 for col in range(5)]
average = [0 for col in range(5)]
grade = [0 for col in range(5)]
rank = [0 for col in range(5)]

#입력 함수
def input_data():
    for i in range(5):
        student[i][0] = input("학번: ")
        student[i][1] = input("이름: ")
        student[i][2] = int(input("영어: "))
        student[i][3] = int(input("C-언어: "))
        student[i][4] = int(input("파이썬: "))

#총점/평균 계산 함수
def calc():
    for i in range(5):
        total[i] = student[i][2] + student[i][3] + student[i][4]
        average[i] = total[i] / 3

#학점계산 함수
def calculate_grade():
    for i in range(5):
        if average[i] >= 90:
            grade[i] = 'A'
        elif average[i] >= 80:
            grade[i] = 'B'
        elif average[i] >= 70:
            grade[i] = 'C'
        elif average[i] >= 60:
            grade[i] = 'D'
        else:
            grade[i] = 'F'

#등수계산 함수
def calculate_rank():
    for i in range(5):
        rank[i] = 1
        for j in range(5):
            if total[i] < total[j]:
                rank[i] += 1

#등수로 정렬
def sort():
    for i in range(4):
        for j in range(4-i):
            if rank[j] > rank[j+1]:
                rank[j], rank[j+1] = rank[j+1], rank[j]
                student[j], student[j+1] = student[j+1], student[j]
                total[j], total[j+1] = total[j+1], total[j]
                average[j], average[j+1] = average[j+1], average[j]
                grade[j], grade[j+1] = grade[j+1], grade[j]

#출력 함수
def output():
    print("성적관리 프로그램\n=============================================================================")
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수\n=============================================================================")
    for i in range(5):
        print(student[i][0], "\t", student[i][1], "\t", student[i][2], "\t", student[i][3], "\t", student[i][4], "\t", total[i], "\t", "{:.2f}".format(average[i]), "\t", grade[i], "\t", rank[i])

input_data()
calc()
calculate_grade()
calculate_rank()
output()