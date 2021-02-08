#Find the sum of middle 3 digit of 5 digit number and if number of digits is not equal 5 then find product of all digit


s = input("Enter the number ")
n = int(s)
print("number of digit {}".format(len(s)))

if(len(s)!= 5):
    mul = 1
    while(n > 0):
        
        mul *= n%10
        n //= 10
        
    print("Product of digit of {} is {}".format(s,mul))

else:           # if digit = 5
    
    sumD = 0
    count = 2
    n //= 10
    
    while(n != 0):
        if(count == 5):
            break
            
        sumD += n%10
        n //= 10
        count+=1
        
    print("Sum of middle 3 digit of {} is {}".format(s,sumD))
    
