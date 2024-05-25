def merge_sort(data):
  """Sorts a list of data in ascending order using merge sort."""
  if len(data) <= 1:
    return data
  # Divide the list into two halves
  mid = len(data) // 2
  left_half = merge_sort(data[:mid])
  right_half = merge_sort(data[mid:])

  # Merge the sorted halves back together
  i = 0
  j = 0
  merged_data = []
  while i < len(left_half) and j < len(right_half):
    if left_half[i] < right_half[j]:
      merged_data.append(left_half[i])
      i += 1
    else:
      merged_data.append(right_half[j])
      j += 1
  # Append remaining elements from either half
  merged_data += left_half[i:]
  merged_data += right_half[j:]
  return merged_data

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = merge_sort(data.copy())  # Avoid modifying original data
print("Original data:", data)
print("Sorted data:", sorted_data)
