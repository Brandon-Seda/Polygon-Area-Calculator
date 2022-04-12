class Rectangle:

  def __init__(self, width, height):
    self.height = height
    self.width = width
  
  def __str__(self):
      return ("Rectangle(width=" + str(self.width) + ", height=" + str(self.height) +")")

  def set_height(self, height):
    self.height = height
    
  def set_width(self, width):
    self.width = width

  def get_area(self):
    area = self.height * self.width
    return area
    
  def get_perimeter(self):
    perimeter = ((2*self.width) + (self.height*2))
    return perimeter

  def get_diagonal(self):
      diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
      return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
        return "Too big for picture."
    picture = (("*" * self.width) + "\n") * self.height 
  
    return picture

  def get_amount_inside(self, other_shape):
      return int(self.get_area() / other_shape.get_area())


class Square(Rectangle):

   def __init__(self, side):
       self.height = side
       self.width = side
   
   def __str__(self):
        return f'Square(side={self.width})'
    
   def set_side(self, side):
       self.width = side
       self.height = side
       



