def count(sequence, item):

  total = 0

  for i in range(0, len(sequence)):
    if sequence[i] == item: total += 1  

  return total


print(count([1, 2, 1, 1], 1))
print(count([1.5, 2.0, 1.6, 1], 1))
print(count([1.5, 2.0, 1.6, 1], [1, 1.5]))


