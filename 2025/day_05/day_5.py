#!/usr/bin/env python3
import os

script_dir = os.path.dirname(__file__)
filename ="input.txt"
filepath = os.path.join(script_dir, filename)

result = 0
isProduct = False
productIdRanges = []
products = []

file = open(filepath)
for line in file:
	if not len(line.rstrip()):
		isProduct = True
		continue

	if not isProduct:
		productIdRange = line.rstrip().split('-')
		productIdRange = list(map(int, productIdRange))
		productIdRanges.append(productIdRange)
	else:
		products.append(int(line.rstrip()))

for product in products:
	print(product)
	isFresh = False
	for productIdRange in productIdRanges:
		if productIdRange[0] <= product and productIdRange[1] >= product:
			result += 1
			break

print("The result is: " + str(result))