import math as Math
class City:
  
  def __init__(self, x, y):
    self.x , self.y = x, y
  
  # Gets city's x coordinate
  def getX(self):
      return self.x

  # Gets city's y coordinate
  def getY(self):
      return self.y
  
    
  #Gets the distance to given city
  def distanceTo(self,city):
    xDistance = abs(self.getX() - city.getX())
    yDistance = abs(self.getY() - city.getY())
    distance = Math.sqrt( (xDistance*xDistance) + (yDistance*yDistance) )        
    return distance
    
    
  def __str__(self):
    return str(self.getX()) + ", " + str(self.getY())
