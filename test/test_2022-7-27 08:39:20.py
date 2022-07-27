def test(num):
    ans =0
    while num:
        ans+=num&1
ans=1
num=55
ans+=num&1
# print(ans)
num>>=1
# print(num)

def solution(num):
    return max(num.bit_count() + num.bit_length() - 1, 0)
# print(solution(10))
# print(ans.bit_count())
