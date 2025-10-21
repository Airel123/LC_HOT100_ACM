import sys


def main():
    n=int(input())
    nums=list(map(int,sys.stdin.readline().strip().split()))

    if n==1:
        print(" ".join(map(str, nums)))
        return

    slow = 0

    for fast in range(n):
        if nums[fast]!=0: 
            nums[slow],nums[fast]= nums[fast],nums[slow]
            slow+=1      
        


    
    print(" ".join(map(str, nums)))
    return


if __name__=="__main__":
    main()
