import urllib.request, urllib.parse, urllib.error

fileStream = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fileStream:
	print(line.decode().strip())
