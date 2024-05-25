def insertion_sort(data):
  """Sorts a list of data in ascending order using insertion sort."""
  for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    # Shift elements of the sorted sub-list to the right to make space for the key
    while j >= 0 and data[j] > key:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = key  # Insert the key element at its correct position
  return data

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = insertion_sort(data.copy())  # Avoid modifying original data
print("Original data:", data)
print("Sorted data:", sorted_data)
