"""
Generated for example#1 writing OOB example in python 3
"""

class Car:
    def __init__(car, brand, model, color, minspeed, maxspeed, year, quantity):
        car.brand = brand
        car.model = model
        car.color = color
        car.minspeed = minspeed
        car.maxspeed = maxspeed
        car.year = year
        car.quantity = quantity

    def sell_car(car, quantity):
        if car.quantity >= quantity:
            car.quantity -= quantity
            print(f"solded {quantity} piece of {car.year} {car.brand}-{car.model} {car.color}. In stock left: {car.quantity}")
        else:
            print("Not available sellable quantity for this car.")

    def update_car(car, quantity):
        car.quantity += quantity
        print(f"Added {quantity} of {car.brand} / {car.model} / {car.color} to stock. New quantity: {car.quantity}")


whitecar = Car("Lotto","A99","White",10,399,2023,5)

whitecar.sell_car(4)
