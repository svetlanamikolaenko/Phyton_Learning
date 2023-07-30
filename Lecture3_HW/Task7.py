# Task 7: File Searching
# Write a Python program that prompts the user to enter a search term 
# and searches for occurrences of that term in a text file named "hw_data.txt". Print the line numbers where the search term is found.

word = input("Enter a search term: ")
with open("Phyton_Learning\Lecture3_HW\hw_data.txt", 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        if line.find(word) != -1:
            print(f'Line number: {lines.index(line)}')