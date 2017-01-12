import random
import copy

class Tour:
  def __init__(self,tourManager,countOfCities):
    self.tour = [None]*countOfCities
    self.distance = 0
    self.countOfCities = countOfCities
    self.tourManager = tourManager

  
  def setTour(self,customTour):
    self.tour = copy.deepcopy(customTour)
    self.distance = 0

  def getTour(self):
    return self.tour

  def generateTour(self):
    for i in range(0,self.countOfCities):
      self.setCity(i,self.tourManager.getCity(i))
    
    #shuffle the Tour
    random.shuffle(self.tour)

  def getCity(self,position):
    return self.tour[position]
    
  def setCity(self,position,city):
    self.tour[position] = city
    #if the tour is changed distance is reset
    self.distance = 0
  
  def getDistance(self):
    if(self.distance == 0):
      tourDistance = 0

      for i in range(0,self.countOfCities):
        fromCity = self.getCity(i)

        if(i+1 < self.countOfCities):
          destinationCity = self.getCity(i+1)
        else:
          destinationCity = self.getCity(0)

        tourDistance += fromCity.distanceTo(destinationCity)

      self.distance = tourDistance

    return self.distance

  def __str__(self):
    separator = "|"
    tourString = separator
    for i in range(0,self.countOfCities):
      tourString += str(self.getCity(i)) + separator
    
    return tourString

