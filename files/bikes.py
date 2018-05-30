# lets define a class bike
class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")


# lets create a couple of instances
red_bike = Bike("Red", "Carbon fiber")
blue_bike = Bike("Blue", "Steel")

# lets inspect the objects we have, instances of the Bike class.
print(red_bike.colour)
# prints: Red

print(red_bike.frame_material)
# prints: Carbon Fibre

print(blue_bike.colour)
# prints: blue

print(blue_bike.frame_material)
# prints: Steel

# let's brake!
red_bike.brake()
# prints: Braking!
