# Let's talk a little bit about classes and objects within Python, 
# which we sneakily introduced in the json-tutorial.py file. 
# First, what is an object? Really, what is an object in reality? 
# It's a "thing" or something that can be percieved by the five senses. 
# Similarily, we can create "objects" or classes in functions - special 
# pieces of code that represent something in reality. For example, let's "define"
# a "car" in Python. 

class car():
    def __init__(self, model_, color, miles):
        self.num_of_wheels = 4
        self.model_ = model_
        self.color = color
        self.miles = miles
        self.insurance_payment = 400
    
    def describe(self):
        description = f'''
            This is a {self.color} {self.model_} with {self.miles} on it. 
            The car has a monthly insurance rate of ${self.insurance_payment}. 
        ''' 
        return description

    def drive(self, addtional_miles):
        self.miles += addtional_miles
        self.insurance_payment += addtional_miles * 0.1

# What the above code does is define a class or an object that represents a car within the real world. 
# You might think that this is something magical or somewhat crazy - afterall, how can we suddenly 
# jump from numbers to making actual cars in code? The truth of the matter is, we aren't. A class, or a blueprint, 
# is simply a collection of variables and methods that we, as humans, attach some sort of meaning to. 
# Quite frankly, Python couldn't care less what we call it - it's just strings of one's and zeros. 
# It is us, as humans, that give it meaning. 

# Okay, so you might be saying that while that's cool, what's the point of it? 
# Well, a whole lot actually. This is actually a distinct stule of coding within the computer science world, 
# known as object-oriented programming. Normally, this is the style that you learn in school/college as well. 
# It has many uses and advantages, some of which we will explore below. 
# NOTE: You usually spend about 4 years with this style of programming. We will be spending 30 minutes. 
# Thus, this tutorial is a great disservice to object-oritented programming and I cannot recommend enough, 
# please, please discover this on your own as well. This IS NOT a sufficient explanation - it's just the basics. 

# Okay, now that we've introduced object-oriented programming, let's talk about some of its use cases. For one, 
# it makes organzing and sorting our data incredibly easy. Let's say that we don't have a car class but we still want to 
# store all of the information about a black Honda, with 1000 miles on it. Well, to do this, we would need about 3
# variables, to store it, which isn't so bad. 

model_ = "Honda"
color = "Black"
miles = 1000

# Okay, so that's not so bad. But how about if we have a 10 cars. A hundred? A thousand? 
# We would need about 3000 variables just to store all that info. Is that even possible?
# Well, yes. But is it reasonable? Of course not! No one wnats to type out a 3000 variables. Just organzing thme 
# would be a nightmare. 

model_list = ["Honda", "Chevy", "BMW", "Ferrari"]
color_list = ["Black", "Red", "White", "Red"]
miles_list = [1000, 4000, 5000, 10000]

# You migth say that we could use lists and indexes to store some of these variables. 
# A valid idea, but then how would we know which is the model, make and number of miles for a particular car?
# How can we keep track of all this data? 

# This is where classes come in. They can help us store all of this information within one variable. 
# which we can then perform some sort of operations on. To but it simply, we can create an instance, 
# or a copy of a class and fill it with the values we need. (The class is really the blueprint we use to make objects). 
# For example, if we want to make a black Honda, with 1000 miles on it, we can simply just write the follwoing. 

car_1 = car("Honda", "Black", 1000)

# Look at that! Just one line and we've created a "car" in virtual space. Quite powerful, isn't it? 
# Before we get too excited, let's review some terminology. 
# Class Fields 
# Class Functions 
# Making a class 


# We won't be doing too much in making our own classes - that's a little bit too advanced for us right now. 
# Let's just instead look at how we can use them. For example, how do we get the "model" class filed of car_1?
# Simple, we just use the . operator and the specify the name of the class field we want to access@ 

print(car_1.model_)
print(car_1.color)
print(car_1.miles)
print("------")

# Awesome! But another great part of classes is that we can also have class functions or functions that 
# are specific to a class. They either do someting with the class fields, with an input variable we give, 
# or some combination of the two. Let's say that we want a description of the car_1, something a little bit more 
# human frienly. Well, the car class has something called a .describe() function, that we can call to get 
# some more info. Let's check it out! 

print(car_1.describe())
print("------")

# Now we have a description! Isn't that exciting? We can scale this method of makign cars and methods to hundreds 
# of millions of data points in a neat and organied manner. It's quite exciting! 
# However, we can also pass in parameters or values to our cars as well. Let's see an example of that@

car_1.drive(100)
print(car_1.miles)
print(car_1.describe())
print("------")

# We can see that after we've "driven" the care an addional 100 miles, the description of the car changes and its 
# insurance rate goes up proprotinally. Note that we did not have to change or modify these values, the functiona 
# automatically handled it for us. Isn't that neat? 

# There is a whole lot more to cover about this topic such as inhertiance, polymorphism, function decorator etc
# that we unfortunately don't have a lot of time for. However, the key takeaway from this class should be clear enough. 
# A class in Python in simply a collection of variables and functions that we give some meaning to. 
# We can create copies of a class, or an instance of the class, called an object. 
# We can then call specific functions for each of these objects to perform some sort of operation on it. 
# This is sinply the basic gist - as long as you udnerstand that a class simply refers to an obect 
# and know how to access the methods and variables of class, this will be enough for now! 


# NOTE: The JSON class should now make some more sense. Whenever we did JSON.loads() in the previous tutorial, 
# we simply called a function fo the JSON class. Note that in this case, the class refers to an obejct 
# that isn't quite tangile (i.e, a file format) but this is okay - it's still a thing! 
# Don't worry too much if this confuses you - we don't really need too much of this. The basics will be enough for now@