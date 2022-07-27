n =15
result=[]
for i in range (1,n+1):
    if i%15==0:
        i ="FizzBuzz"
        result.append(i)
        continue
    if i % 3==0:
        i = "Fizz"
        result.append(i)
        continue
    if i %5==0:
        i = "Buzz"
    result.append(i)
    
print(result)