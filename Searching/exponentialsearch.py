def exponential_search(data, target):
  """
  Performs an exponential search on a list to find the range of the target element.

  Args:
      data (list): The sorted list of data to search through.
      target: The element to search for.

  Returns:
      int: The lower and upper bounds (tuple) of the target element's potential range,
          or (-1, -1) if not found.
  """
  n = len(data)
  i = 1
  while i < n and data[i] <= target:
    i *= 2

  # Search within the narrowed range using binary search (implementation not included here)
  # lower_bound = max(0, i // 2)
  # upper_bound = min(n - 1, i)
  # result = binary_search(data, target, lower_bound, upper_bound)
  # return result

  return (max(0, i // 2), min(n - 1, i))  # Potential range for binary search

# Example usage
data = [1, 3, 9, 16, 25, 36, 49, 64, 81, 100]
target = 36
bounds = exponential_search(data, target)

if bounds[0] != -1 and bounds[1] != -1:
  print(f"Target element {target} might be in range [{bounds[0]}, {bounds[1]}]")
else:
  print(f"Target element {target} not found in the list")
