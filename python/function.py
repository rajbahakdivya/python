# functionto find average marks

def find_average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_of_marks / total_subjects
    return average_marks

# Calculate the grade and return it

def compute_grade(average_marks):
    if average_marks >=80:
        grade= 'A'
    elif average_marks >=60:
        grade= 'B'
    elif average_marks >=50:
        grade='C'
    else:
        grade='F'
    return grade

marks= [55,67,75,80,65] 
average_marks= find_average_marks(marks)
print("Your averege marks is :", average_marks)

grade=compute_grade(average_marks)
print("Your grade is :",grade)