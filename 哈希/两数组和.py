import sys


def main():
    line1 = sys.stdin.readline().strip().split()
    n=int(line1[0])
    target = int(line1[1])
    nums=list(map(int,sys.stdin.readline().strip().split()))

    seen = {}
    for i in range(n): 
        if target - nums[i] in seen:
            print(seen[target - nums[i]],i)
            return
        seen[nums[i]]=i

if __name__ == "__main__":
    main()