# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

dictionary = {}

for i in range(97, 97+26):
    dictionary[chr(i)] = i

print("My Dictionary:\n", dictionary)