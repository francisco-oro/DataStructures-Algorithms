# Question 5 - 2D Lists
# Time complexity: O(n)
# Space complexity: O(1)

def diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if (rows == cols):
        return sum(matrix[i][i] for i in range(rows))
    return -1

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
print(diagonal_sum(myList2D)) # 15