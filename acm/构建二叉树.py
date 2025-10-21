import sys
from collections import deque

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class solution:
    def solution(self):
        nums = list(map(int, sys.stdin.readline().strip().split()))
        if not nums:
            return

        n = len(nums)
        if n == 0 or nums[0] == -1:
            return

        
        nodes = [None if val == -1 else TreeNode(val) for val in nums]
        for i in range(n):
            if nodes[i] is not None:
                left_i = 2 * i + 1
                right_i = 2 * i + 2
                if left_i < n:
                    nodes[i].left = nodes[left_i]
                if right_i < n:
                    nodes[i].right = nodes[right_i]
            

        

        queue = deque()
        queue.append(nodes[0])
        while queue:
            len_ = len(queue)
            for i in range(len_):
                cur = queue.popleft()
                print(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        
        return
    

if __name__ == "__main__":
    solution.solution()