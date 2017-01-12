class TourManager:

  def __init__(self):
    self.tourCities = []

  def addCity(self, city):
    self.tourCities.append(city)
  
  def getCity(self,index):
    return self.tourCities[index]

  def numberOfCities(self):
    return len(self.tourCities)