import urllib.request
import json
import math

def retrieve_all():
    request =  urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(request.read())
    print(data[0])
    temp = []
    for dict in data:
        if dict["enabled"] == False:
            continue
        required_tuple = (dict["fullName"], dict["name"], dict["year"], sum(dict["exercises"]))
        temp.append(required_tuple)
    return temp

def retrieve_course(course_name: str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = json.loads(request.read())
    
    statistics = {}
    # week amount
    statistics["weeks"] = len(data)
    
    # max students_total amount
    maximum_students = hours_total = students_total = exerices_total = 0
    for key in data:
        if data[f"{key}"]["students"] > maximum_students:
            maximum_students = data[f"{key}"]["students"]
        hours_total += data[f"{key}"]["hour_total"]
        students_total += data[f"{key}"]["students"]
        exerices_total += data[f"{key}"]["exercise_total"]
    statistics["students"] = maximum_students
    print(hours_total, students_total)
    # hours total and average
    statistics["hours"] = hours_total
    statistics["hours_average"] = math.trunc(hours_total / maximum_students)
    # exercises total and average
    statistics["exercises"] = exerices_total
    statistics["exercises_average"] = math.trunc(exerices_total / maximum_students)
    return statistics


if __name__ == "__main__":
    retrieve_all()
    print(retrieve_course("CCFUN"))