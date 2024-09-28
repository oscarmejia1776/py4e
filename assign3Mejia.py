# CSCI 2503 - Survey of Programming Languages
# Phillip Mejia
# September 23, 2024
# Program reads a text file of names and grades and then prints the results of the calculations.

# Create a file stream inside of a try except block
try:
  fileStream = open("grades.txt")
except:
  print("File does not exist")
  quit()

# Create Variables
count = 0
total = 0
max = None
min = None
maxName = ""
minName = ""
countAboveAvg = 0
countBelowAvg = 0
pctAboveAvg = 0.0
pctBelowAvg = 0.0
gradeList = list()

# Seperate grade and name on each line
for line in fileStream:
  currentGrade = float(line[line.find(",") + 1:])
  currentName = line[:line.find(",")]

  # Append current grade to grades list
  gradeList.append(currentGrade)

  # Increment the count and sum the grade total
  count += 1
  total += currentGrade

  # Determine max and min grades and names
  if max is None or min is None:
    max = currentGrade
    min = currentGrade
    maxName = currentName
    minName = currentName
  elif currentGrade >= max:
    max = currentGrade
    maxName = currentName
  elif currentGrade <= min:
    min = currentGrade
    minName = currentName

# Calculate average
average = total / count

# Determin counts below / above average
for grade in gradeList:
  if grade < average:
    countBelowAvg += 1
  elif grade > average:
    countAboveAvg += 1

# Calculate percentage below or above average
pctAboveAvg = countAboveAvg / count * 100
pctBelowAvg = countBelowAvg / count * 100

# Print out results
print("Average:", str(average))
print("Maximum: " + str(max) + " (" + str(maxName) + ")")
print("Minimum: " + str(min) + " (" + str(minName) + ")")
print("Grades above average: " + str(countAboveAvg) + ", " + str(pctAboveAvg) + "%")
print("Grades below average: " + str(countBelowAvg) + ", " + str(pctBelowAvg) + "%")