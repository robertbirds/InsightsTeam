# Let's do a live coding session together, crytaliizing some of the things that we have learned so far 
# Your Task: count the number of unique values within a list and store how many copies there are of each 
# value in a dictonary 

value_list = [1,2,3,2,3,3,4,5,6,4,5,6,4,5,6,4,5,6,5,6,6]
value_counts = dict()

unique_values = []
for val in value_list:

    if val not in unique_values:
        value_counts[val] = 1
        unique_values.append(val)
    else:
        value_counts[val] += 1

print("uniqe_values: ", unique_values)
print("value_counts dictonayr: ", value_counts)