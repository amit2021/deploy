class Vehicle:
    color='white'
    def __init__(self ,name,max_speed ,milage,capacity):
        self.name=name
        self.max_speed =max_speed
        self.milage =milage
        self.capacity=capacity

    def seating_capacity(self):
        return('seating capacity of {} is {}'.format(self.name,self.capacity))


    def fare(self):
        return self.capacity*100


