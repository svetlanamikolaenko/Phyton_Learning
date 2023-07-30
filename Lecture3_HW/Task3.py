#Task 3: File Appending
#Write a Python program that prompts the user to enter a line of text and appends it to an existing text file named "hw_data.txt".

with open('Phyton_Learning\Lecture3_HW\hw_data.txt', 'a') as a_writer:
    var = input('Enter your First Name:\n')
    a_writer.write(f'\n{var}')