import math as Math
import random
from City import City
from Tour import Tour
from TourManager import TourManager


def acceptanceProbability(energy, newEnergy, temp):
  if(newEnergy < energy):
    return 1.0
  
  return Math.exp((energy-newEnergy)/temp)

def main():
  tourManager = TourManager()

  city = City(60, 200)  
  tourManager.addCity(city)  
  city2 = City(180, 200)  
  tourManager.addCity(city2)  
  city3 = City(80, 180)  
  tourManager.addCity(city3)  
  city4 = City(140, 180)  
  tourManager.addCity(city4)  
  city5 = City(20, 160)  
  tourManager.addCity(city5)  
  city6 = City(100, 160)  
  tourManager.addCity(city6)  
  city7 = City(200, 160)  
  tourManager.addCity(city7)  
  city8 = City(140, 140)  
  tourManager.addCity(city8)  
  city9 = City(40, 120)  
  tourManager.addCity(city9)  
  city10 = City(100, 120)  
  tourManager.addCity(city10)  
  city11 = City(180, 100)  
  tourManager.addCity(city11)  
  city12 = City(60, 80)  
  tourManager.addCity(city12)  
  city13 = City(120, 80)  
  tourManager.addCity(city13)  
  city14 = City(180, 60)  
  tourManager.addCity(city14)  
  city15 = City(20, 40)  
  tourManager.addCity(city15)  
  city16 = City(100, 40)  
  tourManager.addCity(city16)  
  city17 = City(200, 40)  
  tourManager.addCity(city17)  
  city18 = City(20, 20)  
  tourManager.addCity(city18)  
  city19 = City(60, 20)  
  tourManager.addCity(city19)  
  city20 = City(160, 20)  
  tourManager.addCity(city20)  

  temp = 1000
  coolingRate = 0.003
  heatCoeficient = 1 - coolingRate
  currentTour = Tour(tourManager, tourManager.numberOfCities())
  currentTour.generateTour()
  print("Initial solution distance %d" % currentTour.getDistance())
  print("Initial tour is %s" %currentTour)

  tourBest = Tour(tourManager,tourManager.numberOfCities())
  tourBest.setTour(currentTour.getTour())

  while(temp > 1):
    newTour = Tour(tourManager,tourManager.numberOfCities())
    newTour.setTour(currentTour.getTour())

    tourPos1 = (int)(tourManager.numberOfCities() * random.uniform(0, 1))
    tourPos2 = (int)(tourManager.numberOfCities() * random.uniform(0, 1))

    

    citySwap1 = newTour.getCity(tourPos1)
    citySwap2 = newTour.getCity(tourPos2)

    newTour.setCity(tourPos2, citySwap1)
    newTour.setCity(tourPos1, citySwap2)

    currentEnergy = currentTour.getDistance()
    newEnergy = newTour.getDistance()

    if(acceptanceProbability(currentEnergy, newEnergy,temp) > random.random()):
      currentTour.setTour(newTour.getTour())
    
    if (currentTour.getDistance() < tourBest.getDistance()) :
      tourBest.setTour(currentTour.getTour())
    
    temp *= heatCoeficient

  print("Final slution is :%d" % tourBest.getDistance())
  print("The tour is : %s" % tourBest )

main()