import sys


def main():
    n=int(input())
    nums=list(map(int,sys.stdin.readline().strip().split()))


    l=0
    r=n-1

    V=float('-inf')

    while l<r:
        len_ = r-l
        height_=min(nums[l],nums[r])
        V=max(V,len_*height_)
        if nums[l]>nums[r]:
            r-=1
        else:
            l+=1
    print(V)
    return


if __name__=="__main__":
    main()
