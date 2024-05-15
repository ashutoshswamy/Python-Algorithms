def jump_search(data, target):
  """
  Performs a jump search on a list to find the index of the target element.

  Args:
      data (list): The sorted list of data to search through.
      target: The element to search for.

  Returns:
      int: The index of the target element if found, otherwise -1.
  """
  n = len(data)
  jump = int(n**0.5)  # Optimal jump size for jump search

  # Find the block where the target element might be
  for i in range(0, n, jump):
    curr_end = min(i + jump - 1, n - 1)  # Don't go past list bounds
    if data[curr_end] >= target:
      break

  # Linear search within the block
  for i in range(i, curr_end + 1):
    if data[i] == target:
      return i
  return -1

# Example usage
data = [1, 3, 9, 16, 25, 36, 49, 64, 81, 100]
target = 36
index = jump_search(data, target)

if index != -1:
  print(f"Target element {target} found at index {index} and at position {index + 1}")
else:
  print(f"Target element {target} not found in the list")
