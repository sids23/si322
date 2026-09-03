#solution1.py

#siddharth swarup & nick hogan

#first we want to read the text in numbers into a list
#then we want to sort that data from low to high. 
#then we can loop through that list to print it out

numbers = []

with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(float(line.strip()))

numbers.sort()

#we looked up how to print only certain numbers in the list as a decimal and found this command to format it properly
#we got this from google AI search result
for number in numbers:
    print(f"{number:g}")
