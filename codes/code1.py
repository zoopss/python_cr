class Animal(object):
"""Makes cute animals."""
is_alive = True
health = "Good" 

def __init__(self, name, age):
    self.name = name
    self.age = age

def description(self):
    print self.name
    print self.age 
    print self.is_alive
    print self.health

hippo = Animal("Mary", 02)
sloth = Animal("Larry", 03)
ocelot = Animal("Karry", 04)

hippo.description()
sloth.description()
ocelot.description()
