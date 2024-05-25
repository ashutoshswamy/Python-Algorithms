def selection_sort(data):
  """Sorts a list of data in ascending order using selection sort."""
  for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
      if data[j] < data[min_index]:
        min_index = j
    if i != min_index:
      data[i], data[min_index] = data[min_index], data[i]  # Swap elements
  return data

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = selection_sort(data.copy())  # Avoid modifying original data
print("Original data:", data)
print("Sorted data:", sorted_data)
