#Task 4: File Copying
#Write a Python program that reads the contents of a source file named "source.txt"
#and copies them to a destination file named "destination.txt".

lines = ()
with open("Phyton_Learning\Lecture3_HW\source.txt", "r") as source:
    lines = source.readlines()

with open("Phyton_Learning\Lecture3_HW\destination.txt", "w") as dest:
    dest.writelines(lines)