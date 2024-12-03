class Car:
    wheels = 4 # class variable
    
    def __init__(self,model,color,speed):
        self.model = model  # instance wheel
        self.color = color
        self.speed = speed
    
    def car_stop(self):
        print(f"The {self.color} Car is stopped")
        