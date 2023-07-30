#Task 5: File Line Count
#Write a Python program that reads a text file named "hw_data.txt" and counts the number of lines in the file. Print the line count.
with open('Phyton_Learning\Lecture3_HW\hw_data.txt') as reader:
    lines = reader.readlines()
line_count = len(lines)
print(f'The total count of lines is: {line_count}')

#Task 6: File Word Count
#Write a Python program that reads a text file named "hw_data.txt" and counts the number of words in the file. Print the word count.
with open('Phyton_Learning\Lecture3_HW\hw_data.txt') as reader:
    all_data = reader.read()
    words = all_data.split()
words_len=len(words)
print(f'The total count of words is: {words_len}')
    