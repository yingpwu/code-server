'''
# print(float("inf"))
from time import sleep


amount = 11
coins = [1, 2, 3, 4, 5]
dp = [float("inf")]*(amount+1)
dp[0] = 0
# print(dp)
# print(coins)
for i in range(1, amount+1):
    # for c in coins:
    #     if i-c >= 0:
    #         dpi = dp[i-c]
    #     else:
    #         dpi = float("inf")
    dpi = (dp[i-c] if i - c >= 0 else float("inf") for c in coins)
    for one in dpi:
        print(one)
    print("--------------------------")
    # dp[i]=min(dpi)+1
    # dp[i]=min(dp[i-c] if i -c >=0 else float("inf") for c in coins)+1
    # print(dp[i])
    # sleep(3)
# print(dp[-1])
'''

# with open('./test/index.html') as f:
#     text = f.read()
# print(text)
def test():  
    item = {'t': 'pic', 
    'c': {'ix': 0, 'iy': 0, 'iw': 959, 'ih': 678}, 
    'ps': None, 
    's': {'pic_file': '/home/work/conv//data//bdef/443302355//443302355_1_0.png'},
    'p': {'opacity': 1, 'rotate': 0, 'z': 0, 'w': 959, 'h': 678, 'x': 0, 'y': 0, 'x0': 0, 'y0': 678, 'x1': 0, 'y1': 0, 'x2': 959, 'y2': 0, 'x3': 959, 'y3': 678}}
    
    print(item.get('ps'))                                                                                                                                                                

if __name__ == "__main__":
    test()
