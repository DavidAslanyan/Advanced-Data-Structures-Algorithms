def linearSearch(arr, target):
  for index in range(len(arr)):
    if arr[index] == target:
      return index
  return -1

