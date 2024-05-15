def binary_search(data, target, low=0, high=None):
  """
  Performs a binary search on a sorted list to find the index of the target element.

  Args:
      data (list): The sorted list of data to search through.
      target: The element to search for.
      low (int, optional): Lower bound of the search range (defaults to 0).
      high (int, optional): Upper bound of the search range (defaults to None, meaning the entire list).

  Returns:
      int: The index of the target element if found, otherwise -1.
  """

  if high is None:
    high = len(data) - 1

  if low > high:  # Base case: search range empty
    return -1

  mid = (low + high) // 2  # Calculate the middle index

  if data[mid] == target:  # Target found at the middle
    return mid
  elif target < data[mid]:  # Search the left half if target is smaller
    return binary_search(data, target, low, mid - 1)
  else:  # Search the right half if target is larger
    return binary_search(data, target, mid + 1, high)

# Example usage
data = [1, 3, 9, 16, 25, 36, 49, 64, 81, 100]
target = 36
index = binary_search(data, target)

if index != -1:
  print(f"Target element {target} found at index {index} and at position {index + 1}")
else:
  print(f"Target element {target} not found in the list")
