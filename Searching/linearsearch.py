def linear_search(data, target):
  """
  Performs a linear search on a list to find the index of the target element.

  Args:
      data (list): The list of data to search through.
      target: The element to search for.

  Returns:
      int: The index of the target element if found, otherwise -1.
  """
  for i, element in enumerate(data):
    if element == target:
      return i
  return -1

# Example usage
data = [10, 22, 35, 17, 4, 19]
target = 17
index = linear_search(data, target)

if index != -1:
  print(f"Target element {target} found at index {index} and at position {index + 1}")
else:
  print(f"Target element {target} not found in the list")
