def filter_incorrect():
    with open("lottery_numbers.csv") as filehandle:
        list_to_check = []
        for line in filehandle:
            list_to_check.append(line.strip().replace(";",",").split(","))

    correct_list = []
    for line in list_to_check:
        # valudates if length of list is correct
        if len(line) != 8:
            continue
        # validates if week is right format
        try:
            x = line[0].split(" ")
            y = int(x[1])
        except:
            continue
        # validates if a value is an integer and falls within range
        try:
            number_cheklist = []
            for i in range(1,8):
                validated = True
                current_int = int(line[i])
                if current_int not in range(1,40):
                    validated = False
                    break
                number_cheklist.append(current_int)
            for item in number_cheklist:
                if number_cheklist.count(item) > 1 or not validated:
                    raise ValueError
        except:
            continue
        # formats the line to add to correct list
        formatted_line = line[0] +";"
        for i in range(1,8):
            formatted_line += (line[i] + ",")
        formatted_line = formatted_line[:-1]
        correct_list.append(formatted_line)

    with open("correct_numbers.csv","w") as f:
        for i in correct_list:
            f.write(i + "\n")
        
if __name__ == "__main__":
    filter_incorrect()
