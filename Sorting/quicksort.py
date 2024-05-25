def partition(data, low, high):
  """Partitions the list around a pivot element (Hoare's partition scheme)."""
  pivot = data[high]
  i = low - 1
  for j in range(low, high):
    if data[j] <= pivot:
      i += 1
      data[i], data[j] = data[j], data[i]  # Swap elements
  data[i + 1], data[high] = data[high], data[i + 1]  # Swap pivot to its final position
  return i + 1

def quick_sort(data, low, high):
  """Sorts a list of data in ascending order using quick sort."""
  if low < high:
    # pi is partitioning index, around which the data is partitioned
    pi = partition(data, low, high)
    # Recursively sort elements before and after partition
    quick_sort(data, low, pi - 1)
    quick_sort(data, pi + 1, high)

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
quick_sort(data, 0, len(data) - 1)  # Sort the entire list
print("Original data:", data)
print("Sorted data:", data)
