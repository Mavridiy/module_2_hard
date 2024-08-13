def get_matrix(n, m, value):
    matrix = []
    for j in range (n):
        matrix.append([])
        for i in range (m):
            matrix[j].append(value)
    print (matrix)
get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
