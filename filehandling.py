#Program to open a file and then export the plindrome words to another file Pline.txt
fp= open("C:/Users/maddy/Documents/Genfile.txt","r") # file for read 

file1 = open("C:/Users/maddy/Documents/Paline.txt","a") #file for writting the plainedrome word

file1.write("Below are the Palindrome Words from Genfile.txt \n \n")
for t in fp:
    for word in t.split(" "):
        if word == word[::-1]:           
            file1.write(word+"\n")
            
            
#closing file 
fp.close()
file1.close()
