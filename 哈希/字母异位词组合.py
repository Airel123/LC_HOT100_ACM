import sys
from collections import defaultdict



def main():
    n = int(input())
    str_s = sys.stdin.readline().strip().split()

    # key: sorted str_, value: str_ list
    seen=defaultdict(list)

    for str_ in str_s:
        key = ''.join(sorted(str_))
        seen[key].append(str_)


    for v in seen.values():
        print(" ".join(v))

if __name__ == "__main__":
    main()