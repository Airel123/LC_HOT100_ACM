import sys
from collections import defaultdict
def main():
    n = int(input())

    nums=list(map(int,sys.stdin.readline().strip().split()))

    ans=1
    s=set(nums)
    for i in range(n):
        cur=nums[i]
        if cur-1 not in s:
            len_=1
            while cur+1 in s:
                len_+=1
                cur=cur+1
            ans = max(ans,len_)
    
    print(ans)
    return


if __name__ == "__main__":
    main()