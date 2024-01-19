def is_sorted(arr):
  """
  This function checks if a given array is sorted in ascending order.

  Args:
      arr: A list of numbers.

  Returns:
      True if the array is sorted in ascending order, False otherwise.
  """
  for i in range(1, len(arr)):
    if arr[i-1] > arr[i]:
      return False
  return True
arr = [2,5,3,6,7]
if is_sorted(arr):
  print("The array is sorted in ascending order.")
else:
  print("The array is not sorted in ascending order.")
ar = [1,5,7,9]
if is_sorted(ar):
  print("The array is sorted in ascending order.")
else:
  print("The array is not sorted in ascending order.")

