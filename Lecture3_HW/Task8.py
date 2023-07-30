#Task 8: File Line Reversal
#Write a Python program that reads the contents of a text file named "hw_data.txt" 
#and writes the lines in reverse order to a new text file named "reversed.txt".
reversed_lines = ()
with open('Phyton_Learning\Lecture3_HW\hw_data.txt') as reader:
    lines = reader.readlines()
    reversed_lines = reversed(lines)
    
with open("Phyton_Learning\\Lecture3_HW\\reversed.txt", 'w') as writer:
    writer.writelines(reversed_lines)

