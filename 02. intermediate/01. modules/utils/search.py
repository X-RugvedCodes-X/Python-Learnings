print('Imported search module ... ')

test = 'test string'

def find_index(to_search, target) -> int: 
  for i, value in enumerate(to_search):
    if value == target:
      return i
  return -1