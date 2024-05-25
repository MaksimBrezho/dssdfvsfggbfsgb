import ast

def create_2d_array(input_str):
    array_list = ast.literal_eval(input_str)

    two_d_array = []
    for sublist in array_list:
        row = []
        for num in sublist:
            row.append(num)
        two_d_array.append(row)

    return two_d_array

def min_path_sum(matrix):
    if not matrix:
        return 0
#test
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = matrix[0][0]

    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]

input_string = input()

result_array = create_2d_array(input_string)

result = min_path_sum(result_array)
print(result)
