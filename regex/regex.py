# Import regex library
import re

fileName = input("Enter file: ")

try:
  fileStream = open(fileName)
except:
  print("File does not exist")
  quit()

# Read entire file at one time
readFile = fileStream.read()

# Search for and extract all numbers and store in a list
numbers = re.findall('[0-9]+', readFile)

# Create a sum variable and iterate through list and sum numbers after converting to int
sum = 0
for number in numbers:
  sum += int(number)

# print results
print(sum)
