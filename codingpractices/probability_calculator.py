# 20230206-20230207

import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    colors = list(kwargs.keys())
    for color in colors:
      while kwargs[f"{color}"] > 0:
        self.contents.append(color)
        kwargs[f"{color}"] -= 1

  def draw(self, draw_number: int):
    if len(self.contents) < draw_number:
      return self.contents
    else:
      ret = []
      # draw from the pool draw_number times
      for i in range(0, draw_number):
        x = random.randrange(len(self.contents))
        # get another bunch of random numbers?
        ret.append(self.contents[x])
        self.contents.pop(x)
      return ret

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass
