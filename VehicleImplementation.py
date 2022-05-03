from Vehicle import Vehicle
from bus import  Bus

#
# obj=Vehicle('Vehicle',120,20)
# print(obj.milage)
# print(obj.max_speed)
# print(obj.seating_capacity(300))

obj1=Bus('Bus',100,30,50)
print(type(obj1))
print(isinstance(obj1,Vehicle))
print('Milage of bus is ',obj1.milage)
print('Max speed of of bus is ',obj1.max_speed)
# print(obj1.seating_capacity(capacity=100))
print(obj1.color)
print(obj1.fare())