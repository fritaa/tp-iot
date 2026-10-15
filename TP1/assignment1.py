def calculate_gpa(student_record):
    student_id, student_name, list_of_courses = student_record

    total_weighted_points=0
    total_credit_hours=0

    for corse_code, credit_hours, numerical_grade in list_of_courses:
        total_weighted_points += credit_hours*numerical_grade
        total_credit_hours += credit_hours

    final_gpa=round(total_weighted_points / total_credit_hours, 2) if total_credit_hours > 0 else 0.0

    return (student_name, total_credit_hours, final_gpa)


try:
    #simple demonstration

    sample_course =[
            ("iot",4,2.1),
            ("c",3,4.0),
            ("java",4,3.3)
            ]
    sample_record = ("STU123","islem haj hassine", sample_course)

    summary = calculate_gpa(sample_record)

    print(f"calculater summary : {summary}")
finally :
    print("done")
