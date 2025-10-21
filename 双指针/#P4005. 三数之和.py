import sys

def main():
    n= int(input())
    nums=list(map(int,sys.stdin.readline().strip().split()))


    nums.sort()
    result=[]

    for i in range(n-2):

        if i>0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break 
        l=i+1
        r=n-1
        while l<r:
            sum_=nums[i]+nums[l]+nums[r]
            if sum_==0:
                result.append((nums[i], nums[l], nums[r]))
                l+=1
                r-=1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1              
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1   
            elif sum_<0:
                l+=1
            elif sum_>0:
                r-=1

    for a, b, c in result:
        print(a, b, c)
        
    
if __name__=="__main__":
    main()
        


        