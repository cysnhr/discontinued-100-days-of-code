# 20230206

import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    colors = list(kwargs.keys())
    for color in colors:
      for num in kwargs.values():
        i = int(num)
        while i > 0:
          self.contents.append(color)
          i -= 1
        break

  def draw(self, draw_number: int):
    if len(self.contents) < draw_number:
      return self.contents
    else:
      for i in random.randrange(len(self.contents)):
        ret = []
        ret.append(self.contents[i])
      for i in random.randrange(len(self.contents)):
        self.contents.pop(i)
      return ret

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass
