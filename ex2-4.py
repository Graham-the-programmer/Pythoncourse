exam_mark = int(input("what is exam mark: "))
if exam_mark >= 90:
    print("Grade is A+")
elif exam_mark >= 80 and exam_mark <= 90:
    print("Grade is A")
elif exam_mark >= 70 and exam_mark <= 80:
    print("Grade is B")
elif exam_mark >= 60 and exam_mark <= 70:
    print("Grade is C")
elif exam_mark >= 50 and exam_mark <= 60:
    print("Grade is D")
else:
    print("Grade is Fail")