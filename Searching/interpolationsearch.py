def interpolation_search(data, target):
  """
  Performs an interpolation search on a sorted list to find the index of the target element.

  Args:
      data (list): The sorted list of data to search through.
      target: The element to search for.

  Returns:
      int: The index of the target element if found, otherwise -1.
  """
  low = 0
  high = len(data) - 1

  if low > high:
    return -1

  # Loop until low <= high
  while low <= high:
    # Calculate the interpolation position based on data and target values
    pos = low + ((target - data[low]) * (high - low)) // (data[high] - data[low])

    # Check for exact match at the calculated position
    if data[pos] == target:
      return pos

    # Refine search range based on target comparison
    elif target < data[pos]:
      high = pos - 1  # Search in the left half
    else:
      low = pos + 1  # Search in the right half

  return -1  # Target not found

# Example usage
data = [1, 3, 9, 16, 25, 36, 49, 64, 81, 100]
target = 36
index = interpolation_search(data, target)

if index != -1:
  print(f"Target element {target} found at index {index} and at position {index + 1}")
else:
  print(f"Target element {target} not found in the list")
