

nums = [n for n in range(10)]
nums[::2],nums[1::2]=nums[:len(nums)//2],nums[len(nums)//2:]
print(nums)

print(tuple("test"))

if (1,2) ==(2,1):
    print ("xiangdeng")