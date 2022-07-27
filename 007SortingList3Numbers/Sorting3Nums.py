def two_pointer_sort(arr, lo, hi):
  lop, hip = 0, len(arr) - 1
  index = 0
  while index <= hip:
    if arr[index] == lo:    # swap if the current element is low
        arr[index], arr[lop] = arr[lop], arr[index]
        lop += 1
        index += 1
    elif arr[index] == hi:  # swap if the current element is high, and do not increase index since we have not checked the swapped in element!
      arr[index], arr[hip] = arr[hip], arr[index]
      hip -= 1
    else:                   # we are not sorting middle element
      index += 1

  return arr
