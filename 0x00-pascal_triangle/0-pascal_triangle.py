#!/usr/bin/python3
"""function for Pascal's Triangle"""

# Define a function to generate Pascal's triangle
def pascal_triangle(n):
    # Initialize an empty list to store the rows of the triangle
    result = []
    # Loop from 0 to n-1, where n is the number of rows
    for i in range(n):
        # Initialize an empty list to store the current row
        row = []
        # Loop from 0 to i, where i is the index of the current row
        for j in range(i+1):
            # If j is 0 or i, the value is 1 (the first and last element of each row)
            if j == 0 or j == i:
                row.append(1)
            # Otherwise, the value is the sum of the two elements above it
            else:
                row.append(result[i-1][j-1] + result[i-1][j])
        # Append the current row to the result list
        result.append(row)
    # Return the result list
    return result
