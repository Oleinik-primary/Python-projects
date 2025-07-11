# Write your solution here

# part 1
def add_student(database: list, name: str):
    database[name] = []

def print_student(database: list, name: str):
    if name in database:
        if database[name] == []:
            print(f"{name}:\n no completed courses")
        else:
            sum_for_courses = 0
            print(f"{name}:\n {len(database[name])} completed courses:")
            for i in range(len(database[name])):
                print("  " + database[name][i][0], database[name][i][1])
                sum_for_courses += database[name][i][1]
            print(f" average grade {sum_for_courses / len(database[name]):.1f}")
    else:
        print(f"{name}: no such person in the database")

# part 2
def add_course(database: list, name: str, course_info: tuple):
    found = False
    for i in range(len(database[name])):
        if database[name][i][0] == course_info[0]:
            found = True
            if database[name][i][1] < course_info[1]:
                database[name][i] = course_info
                break  
    if not found and course_info[1] != 0:
        database[name].append(course_info)

# part 4
def summary(database: list):
    print(f"students {len(database)}")
    most_courses = 0
    most_courses_name = best_average_name = ""
    summary_for_courses = best_average = 0
    for name in database:
        for i in range(len(database[name])):
            summary_for_courses += database[name][i][1]
            average = summary_for_courses / len(database[name])
            if average > best_average:
                best_average = average
                best_average_name = name
        if len(database[name]) > most_courses:
            most_courses = len(database[name])
            most_courses_name = name
    print(f"most courses completed {most_courses} {most_courses_name}")
    print(f"best average grade {best_average:.1f} {best_average_name}")