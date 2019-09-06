def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            if grade % 5 == 0:
                result.append(grade)
            else:
                count = 0
                temp = grade
                while temp % 5 != 0:
                    temp += 1
                    count += 1
                if count < 3:
                    result.append(temp)
                else:
                    result.append(grade)
    return result

grades = [73, 67, 38, 33]
print(gradingStudents(grades))