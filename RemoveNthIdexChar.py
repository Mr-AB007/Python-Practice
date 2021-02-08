#Program to remove Nth index from the string

s = input("enter String ")

n = int(input("Enter the nth index of character tyo remove "))

newString = s[0:n] + s[n+1:]

print("New string is '{}'".format(newString))
