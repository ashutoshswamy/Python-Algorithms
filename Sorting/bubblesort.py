def bubble_sort(data):
  """Sorts a list of data in ascending order using bubble sort."""
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(data) - 1):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]  # Swap elements
        swapped = True
  return data

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = bubble_sort(data.copy())  # Avoid modifying original data
print("Original data:", data)
print("Sorted data:", sorted_data)
