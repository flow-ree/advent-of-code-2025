#!/usr/bin/env python3
import os
import hashlib

scriptDir = os.path.dirname(__file__)
filename ="input.txt"
filepath = os.path.join(scriptDir, filename)

total = 0
minVowels = 3

file = open(filepath)
for string in file:
	uncoolStrings = [ "ab", "cd", "pq", "xy"]
	if any(string.find(uncoolString) != -1 for uncoolString in uncoolStrings):
		print(string)
		continue
	vowels = [ "a", "e", "i", "o", "u"]
	vowelsCount = 0
	lastCharacter = None
	doubleFound = False
	for character in string:
		print(character)
		if character in vowels:
			vowelsCount += 1
		if character == lastCharacter:
			doubleFound = True
		lastCharacter = character
	if (vowelsCount >= minVowels and doubleFound):
		total += 1

print("Number of nice strings: " + str(total))