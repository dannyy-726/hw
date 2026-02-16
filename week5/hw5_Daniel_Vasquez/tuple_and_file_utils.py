
#Task 1
def transform_tuple(original_tuple) -> (int,int):
    sum_even = 0
    sum_odd = 0
    
    for num in original_tuple:
        #find the sum of all even numbers
        if num % 2 == 0:
            sum_even += num
        #find the sum of all odd numbers
        else:
            sum_odd += num
    return sum_even,sum_odd


#Task 2
def unique_letters(string1:str,string2:str) -> (set,set,set):
    str1 = set(string1)
    str2 = set(string2)

    #find characters unique to string 1
    str1_unique = str1 - str2
    
    #find characters unique to string 2
    str2_unique = str2 - str1

    #find char in both strings
    str1_str2 = str1 & str2

    return str1_unique,str2_unique,str1_str2

#Task 3
def grade_summary(student_grades:dict) -> dict:
    result = {}

    for student in sorted(student_grades):
        grades = student_grades[student]
        avg_grade = round(sum(grades)/len(grades),2)
        max_grade = max(grades)

        result[student] = {"average":avg_grade,
                           "highest":max_grade}
    return result

#Task 4
def read_students(file_name:str) -> dict:
    import csv
    students = {}

    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) < 2:
                continue
            name = row[1]
            grades_raw = row[2:]

            grades = []
            for grade in grades_raw:
                if grade.strip() != "":
                    grades.append(int(grade))
            students[name] = grades
    return students

def write_averages(file_name: str, averages: dict):
    import csv

    with open(file_name, mode = 'w', newline = '' ) as file:
        writer = csv.writer(file)

        writer.writerow(["student_id", "student_name", "average_grade", "highest"])

        student_id = 1

        for name in averages:
            avg = averages[name]["average"]
            highest = averages[name]["highest"]

            writer.writerow([student_id, name, f"{avg:.2f}",highest])
            student_id += 1

    
    


