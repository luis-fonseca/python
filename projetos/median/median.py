def median(lst):

  length = len(lst)
  division = length // 2
  remainder = length % 2

  lst = sorted(lst)  

  # checa se é um número ímpar de itens
  # retorna o valor do índice da metade da lsta
  if remainder > 0:
    return lst[(division)]

  # caso for um número par de itens
  # retorna a média dos dois números do meio
  total = (lst[(division)] + lst[(division - 1)])
  total /= 2.0 # necessário para retornar a casa decimal

  return total
  


print(median([7, 12, 3, 1, 6]))
print(median([7, 3, 1, 4]))
print(median([4, 5, 5, 4]))
