"""
Recipe for a hot beverage that the CoffeeMaker can make.
A recipe can contain coffee, sugar, milk, chocolate, and water.
Units are not specified.
"""
from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    coffee: int
    chocolate: int
    milk: int
    sugar: int
    price: float

    def __init__(self, name):
        self.name = name
        self.coffee = 0
        self.chocolate = 0
        self.milk = 0
        self.sugar = 0
        self.price = 0.0

    def create_recipe(self, coffee=0, chocolate=0, milk=0, sugar=0, price=0):
        self.coffee = coffee
        self.chocolate = chocolate
        self.milk = milk
        self.sugar = sugar
        self.price = price
