(*FIRST,) = [1, 2, 3]  # documenting code no fun
*FIRST, a, b = [1, 2, 3]  # documenting code no fun
a, b = [1, 2]  # documenting code no fun

def foo():
  """
  """
  pass

def wrong_callable():
    number = ImaginaryNumber()
    if callable(number):
        return number()


def bar():
  items = []
  for i in range(2):
    items.append(i)
  return items
