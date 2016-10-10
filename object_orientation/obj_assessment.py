"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Having classes makes possible:
subclasses that inherit attributes and methods from their parent. This allows us
to make variations of the parent rather easily.
Keeps the code from being overly long, confusing, or repetitive.
-abstraction:
 don't need to let the user know all the intricacies of how certain functions work
-encapsulation:
 data is bundled with the functions that work on that data
-polymorphism:
 functions or methods can be applied to more than one subclass — general enough


2. What is a class?
It's a "type" of object that a coder can create, and it usually has a template
of attributes and that its subclasses can take on

3. What is an instance attribute?
A piece of information that you add on to an object of a class

4. What is a method?
A function that operates on a class it is defined within, called like Class.method()

5. What is an instance in object orientation?
It's an object that you create of your type Class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
Class attribute is assigned when you first create your class, and all the instances
of that class get assigned that same attribute.  It is within your template.
Instance attribute is assigned after you create your object of your type class,
and it can overwrite class attributes.  You can also add new instance attributes
without affecting any of the other instances of the same class.

"""


# Parts 2 through 5:
# Create your classes and class methods

class AbstractFood(object):
    """ A thing that you eat. """
    def __init__(self, name):
        self.name = name

    def speak(self):
        """ In this alternate universe, foods may speak. Notice I did not say 'can.' """
        print "Hi, I'm %s and I know you're hungry but wait a second." % self.name

class MeatDish(AbstractFood):
    """ Food with meat. """
    def __init__(self, name, meat_type):
        super(MeatDish, self).__init__(name)
        self.meat_type = meat_type  # pork, shrimp, chicken, or beef

    def speak(self):
        """ Meats speak as well. """
        super(MeatDish, self).speak()
        print "I'm a %s dish." % self.meat_type

    def fight(self):
        """ This plate fights back. """
        print "* Slaps your fork away *"

class VegetarianDish(AbstractFood):
    """ Food without meat. """
    def __init__(self, name, main_veg):
        super(VegetarianDish, self).__init__(name)
        self.main_veg = main_veg

    def speak(self):
        """ Veggies speak as well. """
        super(VegetarianDish, self).speak()
        print "I'm a mostly %s dish." % self.main_veg

    def fight(self):
        """ This plate also fights back. """
        print "* Crawls away *"
