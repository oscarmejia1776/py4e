fileName = input("Enter file: ")

try:
  fileStream = open(fileName)
except:
  print("File does not exist")
  quit()

emails = dict()

for line in fileStream:
  words = line.split(" ")
  if (words[0] == "From" and len(words) > 3):
    email = words[1]
    emails[email] = emails.get(email, 0) + 1

bigEmail = None
bigCount = None

for email, count in emails.items():
  if bigCount is None or count > bigCount:
    bigCount = count
    bigEmail = email

print(bigEmail, bigCount)
