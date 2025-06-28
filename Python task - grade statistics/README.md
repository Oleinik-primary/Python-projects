Description of a task solution from "Grade statistics" task from Python Programming MOOC 2023 https://programming-23.mooc.fi/part-4/6-strings-and-lists

## Result
Even though the code ended up being twice as long and more verbose unlike the presented solution, this task definitely solidifed fundamental list, loop, function concepts as well as methods for working with sequences (strings and lists)
- Personal solution: grade_satistics.py
- Intended solution: grade_satistics_solution.py
## Functions description
- **final evaluation** - ask input as per the task's description, calling 4 other functions: exam_statistics, final_list_split, exam_grades, failed_count
- **final_list_split** - splits input list and summarizes a student's score
- **pass_list** - lists students who have passed *before the exam* (see problem 2)
- **failed_count** - lists students who have failed *before the exam* (see problem 2)
- **exam_grades** - grades students based on pass_list result
- **exam_statistics** - prints exam statistics as per task's desription

## Thought process and encountered problems
Initial draft of the full code actually encountered minimal errors. Draft functions worked as per the initial solution idea. Naturally, the program as a whole was not working as intended as was discovered during testing, but encountering only one error prior to program's start was uplifting.

- Problem 1. Small issue prior to a bigger one was ZeroDivisionError: in exam_statistics, len(some_list) was evaluating to 0 if no students got to the exam in the first place (<10 exam points)
  - Solution: resolved itself after solving problem 2
- Problem 2. The big issue. While not initially apparent, in this task students who have <10 exam points should not be graded at all, **but their score points remain**. This caused an issue where two groups of students appear: those who failed prior to the exam and those who failed during, which impacted program output, because in the end the total score should be considered for ***both*** groups
  - Solution: to make the program work, I split it in two separate lists: those who passed and failer prior to the exam. Afterwards, passers were graded only. In the final output, amount of 0 students is a sum of those who failed during exam and those who did not get to the exam at all.

## To improve

- Less verbose functions for clarity
- Shorter code solutions
