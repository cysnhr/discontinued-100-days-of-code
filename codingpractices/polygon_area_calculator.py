class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      output = ""
      for i in range(0, self.height):
        output += "*" * self.width + "\n"
    return output
  def get_amount_inside(self, shape):
    if shape.__class__ == Square:
      if self.width < shape.width or self.height < shape.width:
        return 0
      else:
        return (self.height // shape.width) * (self.width // shape.width)
    if shape.__class__ == Rectangle:
      if self.width < shape.width or self.height < shape.height:
        return 0
      else:
        return (self.height // shape.height) * (self.width // shape.width)

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
  def __repr__(self):
    return f"Square(side={self.width})"
  def set_side(self, side):
      super().set_height(side)
      super().set_width(side)
  def set_width(self, side):
        super().set_height(side)
        super().set_width(side)
  def set_height(self, side):
        super().set_height(side)
        super().set_width(side)
        
 rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
