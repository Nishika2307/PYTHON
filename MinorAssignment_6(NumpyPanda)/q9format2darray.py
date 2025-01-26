import numpy as np

def format_2d_array(arr):
    # Convert input to NumPy array (if it's not already)
    arr = np.array(arr)
    
    # Find the maximum element in the array
    max_element = arr.max()
    
    # Determine the width of the largest element
    width = len(str(max_element))
    
    # Format the array
    formatted_rows = []
    for row in arr:
        # Format each element in the row to be right-aligned
        formatted_row = " ".join(f"{elem:>{width}}" for elem in row)
        formatted_rows.append(formatted_row)
    
    # Join all rows with newline characters
    return "\n".join(formatted_rows)

# Example usage
array = np.array([
    [1, 23, 456],
    [7890, 12, 34],
    [567, 890, 1234]
])

formatted_string = format_2d_array(array)
print(formatted_string)

'''
   1   23  456
7890   12   34
 567  890 1234'''
 