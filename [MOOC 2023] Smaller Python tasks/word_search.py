# Write your solution here

def find_words(search_term: str):
    # saves words from file in list
    derived_words = []
    matched_words = []
    with open("words.txt") as main_file:
        for line in main_file:
            derived_words.append(line.strip())
    # dot functionality
    if "*" not in search_term:
        for word in derived_words:
                if len(word) == len(search_term):
                    check = 0
                    for index in range(len(word)):
                        if search_term[index] != word[index] and search_term[index] != ".":
                            break
                        else:
                            check += 1
                    if check == len(word):
                        matched_words.append(word)
    # asterisk funtionality
    else:
        if search_term.startswith("*"):
            for word in derived_words:
                if word.endswith(search_term[1:]):
                    matched_words.append(word)
        elif search_term.endswith("*"):
                for word in derived_words:
                    if word.startswith(search_term[:-1]):
                        matched_words.append(word)
    return matched_words


if __name__ == "__main__":
    print(find_words("*thing"))