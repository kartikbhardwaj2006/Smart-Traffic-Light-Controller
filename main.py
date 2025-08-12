# this is my first python project 
import time

RED = "RED"
YELLOW = "YELLOW"
GREEN = "GREEN"

DIRECTIONS = ["North", "East", "South", "West"]

class TrafficLight:
    def __init__(self, direction):
        self.direction = direction
        self.state = RED
    
    def change_state(self, state):
        self.state = state
        print(f"Traffic light at {self.direction} is {self.state}")

class TrafficManagementSystem:
    def __init__(self):
        self.lights = {direction: TrafficLight(direction) for direction in DIRECTIONS}
        self.light_times = {direction: {RED: 5, YELLOW: 2, GREEN: 7} for direction in DIRECTIONS}
    
    def get_traffic_density(self, direction):
        while True:
            try:
                density = int(input(f"Enter the number of cars at {direction} (0-20): "))
                if 0 <= density <= 20:
                    return density
                else:
                    print("Please enter a number between 0 and 20.")
            except ValueError:
                print("Invalid input. Please enter an integer value between 0 and 20.")
    
    def adjust_cycle(self, direction):
        density = self.get_traffic_density(direction)
        print(f"Traffic density at {direction}: {density} cars")
        
        if density < 1:
            self.light_times[direction].update({GREEN: 1})
        elif density < 5:
            self.light_times[direction].update({GREEN: 10})
        elif density < 10:
            self.light_times[direction].update({GREEN: 15})
        elif density < 15:
            self.light_times[direction].update({YELLOW: 3, GREEN: 20})
        else:
            self.light_times[direction].update({RED: 7, YELLOW: 4, GREEN: 25})

    def run(self):
        while True:
            for direction in DIRECTIONS:
                self.adjust_cycle(direction)
                self.lights[direction].change_state(GREEN)
                time.sleep(self.light_times[direction][GREEN])
                self.lights[direction].change_state(YELLOW)
                time.sleep(self.light_times[direction][YELLOW])
                self.lights[direction].change_state(RED)
                time.sleep(self.light_times[direction][RED])

traffic_system = TrafficManagementSystem()
traffic_system.run()
