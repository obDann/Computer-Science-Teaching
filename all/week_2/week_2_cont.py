# Tuples
some_tuple = (1, "a", 2, True, 69)
print(some_tuple)
print(some_tuple[1])
#some_tuple.append(5)
#some_tuple.remove(1)
# as opposed to a list
some_list = [1, 2, 3, 4, 5]
some_list.append(3)
some_list.remove(5)
print(some_list)

# Dictionaries
my_dict = {True: 23, "my_string": False, 44: "some_string", True: 43}
# accessing values:
print(my_dict["my_string"])


my_set = set()
for i in range(10):
    my_set.add(i)

my_set.add("a")
my_set.add("b")
my_set.add("c")
my_set.add("d")
print(my_set)


# importing
from import_demo import some_function
some_function()


# reading files
file_handle = open("this_demo_text_file.txt", "r")

# reading file per line at a time (manually)
#my_str = file_handle.readline()
#my_str = file_handle.readline()

## read the whole file and save it into a variable
#my_str = file_handle.read()
#print(my_str)

# reading the whole file as a list
##my_str = file_handle.readline()
##my_str = file_handle.readline()
file_list = file_handle.readlines()
print(file_list)

#for line in file_handle:
    #some_var = line.strip()
    #print(some_var)

file_handle.close()

# Writing/Appending to files
new_file_handle = open("this_demo_text_file.txt", "a")

adding_str = "Hey this is a string to be added"
# the new line is not added once you write it
new_file_handle.write("\n" + adding_str)

new_file_handle.close()