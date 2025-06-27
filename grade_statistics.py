
# if person has < 10 exam score: points remain, no grade, add to failed (0)
# if person has > 10 exam score but fails anyway: points remain, grade, add to failed (0)

def final_evaluation():
    results_list = []
    while True:
        next_result = input("Exam points and exercises completed:")
        if next_result == "":
            exam_statistics(results_list, 
                            final_list_split(results_list),
                            exam_grades(pass_list(results_list)),
                            failed_count(results_list))
            break
        else:
            results_list.append(next_result)
            continue

def final_list_split(results_list):
    split_list = []
    for i in results_list:
        i_list = i.split(" ")
        i_sum = int(i_list[0]) + (int(i_list[1]) // 10)
        split_list.append(i_sum)
    return split_list

def pass_list(split_list):
    pass_list = []
    for i in split_list:
        i_list = i.split(" ")
        if int(i_list[0]) >= 10:
            i_sum = int(i_list[0]) + (int(i_list[1]) // 10)
            pass_list.append(i_sum)
    return pass_list

def failed_count(results_list):
    failed_count = 0
    for i in results_list:
        i_list = i.split(" ")
        if int(i_list[0]) < 10:
            failed_count += 1
    return failed_count

def exam_grades(pass_list):
    exam_grades = []
    for i in pass_list:
        if i in range(0, 15):
            exam_grades.append(0)
        elif i in range(15,18):
            exam_grades.append(1)
        elif i in range(18,21):
            exam_grades.append(2)
        elif i in range(21,24):
            exam_grades.append(3)
        elif i in range(24,28):
            exam_grades.append(4)
        elif i in range(28,31):
            exam_grades.append(5)
    return exam_grades

def exam_statistics(results_list, split_list, exam_grades, failed_count):
    grades = [5,4,3,2,1,0]
    exam_avg = sum(final_list_split(results_list)) / len(split_list)
    if len(exam_grades) == 0:
        pass_percent = 0
    else:
        pass_count = 0
        for i in grades:
            if i != 0:
                pass_count += exam_grades.count(i)
        pass_percent = (pass_count / (len(exam_grades) + failed_count))*100
    print("Statistics:")
    print(f"Points average: {exam_avg:.1f}")
    print(f"Pass percentage: {pass_percent:.1f}")
    print("Grade distribution:")
    for i in grades:
        if i != 0:
            print(f"\t{i}:", "*" * exam_grades.count(i))
        else:
            print(f"\t{i}:", "*" * (exam_grades.count(i) + failed_count))

final_evaluation()
