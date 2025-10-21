import sys

# excel思路：
# 1) 先判断首行/首列是否有0，单独用两个布尔变量记下来
# 2) 用首行和首列作为标记位：从第2行第2列开始，遇0则把该行首位和该列首位置0
# 3) 根据标记清零第2..m行与第2..n列
# 4) 最后根据布尔变量清零首行/首列

def main():
    m, n = map(int, sys.stdin.readline().strip().split())  # m行, n列
    matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

    # 1) 首行、首列是否含0
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # 2) 用首行首列做标记（从第2行第2列开始）
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # 3) 按标记清零（第2..m行）
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    # 3) 按标记清零（第2..n列）
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    # 4) 处理首行、首列
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

    # 按题意逐行输出
    for i in range(m):
        print(" ".join(str(x) for x in matrix[i]))

if __name__ == "__main__":
    main()
