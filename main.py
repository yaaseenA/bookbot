def printReport(input_dictionary):
    dictList = []
    
    for item in input_dictionary:
        if item.isalpha():
            new_dictionary = {
                item: input_dictionary[item]
            }

            dictList.append(new_dictionary)   

    # python is retarded for this
    dictList.sort(key=lambda d: next(iter(d.values())), reverse=True)

    for item in dictList:
        for char, count in item.items():
            print(f"The '{char}' character was found {count} times")

def countChars(text):
    # print how many times each char appears
    dictionary = {}

    for letter in text.lower():
        if letter not in dictionary:
            dictionary[letter] = 1
        else: 
            dictionary[letter] += 1

    return dictionary


def countWords(words):
    # print total word count
    count = 0
    for word in words.split():
        count += 1

    return count
   

def main():

    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(countWords(file_contents))
        # print(countChars(file_contents))
        printReport(countChars(file_contents))


main()