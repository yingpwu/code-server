num=123
def test(num):
    count=0
    def fib_test(num):
        nonlocal count
        if num!=1:
            if num%2==0:
                num=num//2
            else:
                num-=1
            count+=1
            return fib_test(num)
        else:
            return count+1

    print(fib_test(num))
