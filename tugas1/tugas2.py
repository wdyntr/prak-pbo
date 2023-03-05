def validate_dimension(dimension):
    # Check if the dimension is valid (i.e. it has length 2)
    if len(dimension) != 2:
        print(-1)
        return False
    else:
        return True

def read_array():
    # Read the dimension of the array from the user
    rows, cols = map(int, input().split())

    # Check if the dimension is valid
    if not validate_dimension([rows, cols]):
        exit()

    # Initialize an empty array
    arr = []

    # Read the elements of the array from the user row by row
    for i in range(rows):
        row = list(map(int, input().split()))
        arr.append(row)

    # Check if the length of the row is valid
    if len(row) != cols:
        print(-1)
        exit()

    return arr

def transpose_array(arr):
    # Compute the transpose of the array
    transposed_arr = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    return transposed_arr

def print_array(arr):
    # Print the array row by row
    for row in arr:
        print(" ".join(str(x) for x in row))
        
array = read_array()

transposed_array = transpose_array(array)

print_array(transposed_array)