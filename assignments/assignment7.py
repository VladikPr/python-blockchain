# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).

class Food:
   def __init__(self, name, kind):
      self.name = name
      self.kind = kind

   def describe(self):
      print(f'Name: {self.name}, Kind: {self.kind}')

food1 = Food('potato', 'vegetables')
food1.describe()
# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.
# class Food:
#    def __init__(self, name, kind):
#       self.name = name
#       self.kind = kind

#    @staticmethod
#    def describe(name, kind):
#       print(f'Name: {name}, Kind: {kind}')

# Food.describe('apple', 'fruits')

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.
# 4) Overwrite a “dunder” method to be able to print your “Food” class.
class Meat(Food):
   def cook(self):
      print('''
      Blue: 1 min each side
      Rare: 1.5 min each side
      Medium rare: 2 mins per side
      Medium: 2.5 min per side
      Well-done steak: Cook for about 4-5 mins each side
      ''')

meat = Meat('Beef', 'meat')
meat.cook()

class Fruit(Food):
   def __init__(self, name, weight):
      super().__init__(name, 'fruit')
      self.weight = weight
   def __repr__(self):
      return '''
         To wash a large amount of produce, such as an entire head of lettuce or kale or a bag of apples, use your kitchen sink. For a smaller amount of fresh fruit, vegetables, or herbs such as a bunch of cilantro or a pint of blueberries, use a large, clean mixing bowl.
      '''

fruit = Fruit('orange', '131g')
print(fruit)

