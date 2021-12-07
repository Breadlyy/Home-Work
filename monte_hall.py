import random

def place_car():
    num = random.randint(1,3);
    return num

def player_choice(num):
    return num

def open_doors(nums = [1,2,3]):
    nums.remove()

class MontyHallSim():

  def __init__(self, roundCount):
    self.roundCount = roundCount;

  def runRound(self, requestChange):
    self.roundCount=+1
    car = random.randint(1,3);
    doors = [1,2,3]
    choice = int(input())
    doors.remove(choice)
    doors.remove(car)
    print("Behind the" + doors[0] + "is goat")
    next_choice = int(input("Yes or no"))
    if next_choice == "no":
        pass



    # run one rund
    # 1. car is randomly placed behind one of the doors
    # 2. player select a random door
    # 3. host opens another door (i.e. other than player's choice) with NO car behind 
    # 4. if requestChange == True player selects another door
  
  def run(self, requestChange):
    self.requestChange = requestChange;
    
    # run roundCount runds

sim = MontyHallSim(100000)
print("Chance to win if...")
print("player request NO change: ", sim.run(False))
print("player request change: ", sim.run(True))



