# Today we will talk about fucntions and how they are useful in Python 
# Hint: we've already been using a lot of these! This is just a more formal introduction! 
# First, let's examine what the following piece of code does. 
# Can you figure it out?

myList = [12,49,68,20,2,78,13,777,454,65]
mystery = []

for elem in myList:
    if elem > 50:
        mystery.append(elem)

mystery.sort()
print(mystery)

# Okay, but lets say that I want to do this for another list. Maybe 10 or more. Or maybe a 100. 
# Can you see how this would be really annoying and troublesome to code? Not to mention inefficient?
# This is where functions come in! Simply put, a function is a series of instructions to be applied 
# to a set of inputs, which then returns an output. It is not all to dissimilar to a function in mathmatics! 

# To define a function we use the def keyword, followed by the name of the function, open parentheses, 
# the parameters we want the function to accept, closed parentheses, followed by a semicolon. 
# While this takes a bit to type out, it is much easier to see in code! 

def demo_function(param1, param2):
    return 0

# Note that each time we use the semicolon, we will always indent our blocks, similar to what we see when we 
# did our if/else statements. However, you might have also spotted the return keyword, which might surprise you. 
# Well, what does that do? It simply tells the function what to return. It is analogous to the output of a mathmatical function. 
# Let's see it in action. To call a function, we simply write the name of the function, followed by the parameters we want to
# pass to it. 

demo = demo_function(10,7)
print("Demo: ", demo)

# In this case, we see that demo is 0. Exactly what we expect since the demo_function only return 0, no matter the 
# inputs. Let's say we want to add the inputs we give to the demo_function. How would we do that then?
# Well, in this case, we have to manipulate the function inputs in the body of our function and then return them!
# NOTE: EXTREMELY IMPORTANT --> SCOPE!
#   Function parameters only exist in the function itself and does not affect anything outside of it! 
#   This means that anything defined within the function itself cannot be accessed outside of it. For example,  
#   if I created a variable called apple within the function, I could not print apple (or acess its value)
#   outside of the function itself. It exsists only within the function itself. This also follows true for 
#   any paramters your pass into the function - these parameters will only be a copy of the actual values and
#   will not be affected by any changes within your work. This is an extremely important idea to learn 
#   and we will talk about this more when we speak of classes and objects. 

def get_sum(val1, val2):
    defined_sum = val1 + val2

    val1 = 0
    val2 = 1
    return defined_sum

a = 10
b = 15
result = get_sum(a, b)

# In this case, what is the value of a, b and result after line 57? 
# Why are these the values?

print("\na is: ", a)
print("b is: ", b)
print("result is: ", result)

# What is wrong with the following line of code? 
# What is this a problem of?

# print(defined_sum)

# To continue, please comment out the line above. 
# To see the power of functions, let's extrapolate out our previous example into something a little 
# more robust. 

def mystery_func(aList, to_compare):
    to_return = []

    for elem in aList:
        if elem > to_compare:
            to_return.append(elem)
    
    to_return.sort()
    return to_return

# Examine the function above. How is it more robust, or more useful, than the process we did in the beginning? 
# Let's use it and see what happens! 

list1 = [12, 49, 68, 20, 2, 78, 13, 777, 454, 65]
list1_results = mystery_func(list1, 50)
print("\nList1: ", list1, "\nList1_results: ", list1_results)

list2 = [88, 62, 38, 37, 90, 70, 4, 78, 49, 72]
list2_results = mystery_func(list2, 10)
print("\nList2: ", list2, "\nList2_results: ", list2_results)

list3 = [10, 93, 98, 47, 78, 77, 40, 1, 67, 19]
list3_results = mystery_func(list3, 70)
print("\nList3: ", list3, "\nList3_results: ", list3_results)

# Can you see how functions are wildly useful? It can shrink an intense set of instructions 
# into a line that you can use over and over! 
# To fully empahsize how useful this is, here's a real world example of a function that someone could write. 
# While this is not exactly analogous to how I use it, this should serve as a good example. 
# Note that all data in this case is simulated - the underlying principles are the same however.
# Note that for this example, I've fully documented and written out the function. This is an example 
# of how a function may appear in a production-ready library. You may choose to adopt this style 
# if you plan on using your functions more than once and don't want to have to remember much (I hihgly recommend it!)
# and to get yourself into the swing of things. Not documenting or using some of these checks is fine 
# if you wish to use it for your own project or files. 

IP_Adresses = ["4.118.80.67", "129.190.24.233", "193.60.5.186", "208.206.49.111", "224.30.118.112", "247.9.35.179", 
                "255.34.162.196", "249.116.89.183", "129.109.225.94", "111.150.77.61"]

def check_range(ip):
    '''
        Author: Rashed Rifat 
        Determines the class of an IP Address according to conventional guidelines. 
        
        Args:
            ip (str): the IP Address to determine the class of 
        Returns:
            str:    a letter representing the class of the IP Address 

    '''

    # Check to see if ip is of class str and formatted properly 
    if not isinstance(ip, str):
        raise TypeError(str(ip) + "is of type " + str(type(ip)) + " not str")

    try:
        ip = int(ip.split(".")[0])
    except:
        raise ValueError("IP not formatted properly. Please ensure it is in XXX.XXX.XXX format.")

    # Use if statemented to determine the class of the IP Adress 
    # A switch statement (to be covered later) may have been more advisiable 
    if (ip >= 1 and ip <= 9) or (ip >= 11 and ip <= 126):
        return "A"
    elif (ip >= 128 and ip <= 171) or (ip >= 173 and ip <= 191):
        return "B"
    elif (ip >= 192 and ip <= 195) or (ip >= 197 and ip <= 223):
        return "C"
    elif (ip >= 224 and ip <= 247):
        return "D"
    elif (ip >= 248 and ip <= 255):
        return "E"
    else:
        raise ValueError("Incorrectly formatted IP." )

# Now imagine having to rewrite all of that code each and every time you wanted to use 
# it to check the range of an IP Address. Crazy right?
# Instead, I can check hundreds of thousands of IP Addresses with a single command! How cool is that?!?

print("\n\n")
for ip in IP_Adresses:
    print("IP", ip, "is of class", check_range(ip))