stud_list = [ 'Alice','Bob', 'Carrie','David','Ella','Fendy','Grace']
score_list = [90,87,37,65,89,77,90]

def topstudent(stud_list,score_list):
    highest_score = max(score_list)
    student_with_highest_score = []
    for i in range (len(score_list)):
        if score_list[i] == highest_score:
            student_with_highest_score.append(stud_list[i])
    return student_with_highest_score

student_with_highest_score = topstudent(stud_list,score_list)
print(student_with_highest_score)
