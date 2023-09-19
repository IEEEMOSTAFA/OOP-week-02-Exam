#Use of Inner function:
def calculate_triangle_area(base,height):

  def calculate_area(base,height):
    return 0.5*base*height
  return calculate_area(base,height)        


triangle_area = calculate_triangle_area(10,5)
print(triangle_area)