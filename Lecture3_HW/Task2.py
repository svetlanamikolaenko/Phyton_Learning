#Task 2: File Writing
#Write a Python program that prompts the user to enter some text and saves it to a text file named "output.txt".
with open('Phyton_Learning\Lecture3_HW\output.txt', 'w') as file:
    var = input('Enter your First Name:\n')
    file.write(f'{var}\n')