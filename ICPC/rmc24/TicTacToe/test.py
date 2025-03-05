def remove_elements(array1, array2):
  """Removes elements from array1 that are present in array2."""

  result = [x for x in array1 if x not in array2]
  return result

array1 = [1, 2, 2, 2, 3, 3, 3, 4, 5]
array2 = [3, 5]

result = remove_elements(array1, array2)
print(result)