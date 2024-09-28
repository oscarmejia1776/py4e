fileName = input("Enter file: ")

try:
  fileStream = open(fileName)
except:
  print("File does not exist")
  quit()

# Create tuple
hours = {}
for line in fileStream:
  words = line.split(" ")

  # Separate hour and then determine if its in the tuple, then increment
  if line.startswith("From") and len(words) > 3:
    hour = words[6][:2]
    hours[hour] = hours.get(hour, 0) + 1

# Sort then print out results
for hour, count in sorted(hours.items()):
  print(hour, count)

fileStream.close()