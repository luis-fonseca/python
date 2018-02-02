def remove_duplicates(lst):

  new_list = []
  
  for item in lst:
    if not item in new_list:
      new_list.append(item)
    
    
  return new_list


print(remove_duplicates([1, 2, 1, 3]))
