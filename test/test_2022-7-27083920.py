num=123
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


<%*
const content = tp.file.content.split("/n").map(line => {if (line.includes("status:")) {line = "status: :green_square:"}return line}).join("\n")
const file = tp.file.find_tfile(tp.file.title)
await app.vault.modify(file, content)
%>