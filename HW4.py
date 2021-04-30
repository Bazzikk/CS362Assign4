

# Returns the volume of a cube using a side length
def find_cube_volume(l):
    return  l * l * l

# i = 4
# print(find_cube_volume(int(i)))


# Returns the average value from the values in the list
def list_average (list):
    total = 0
    for i in list:
        total = total + i
    avg = total / len(list)
    return avg

# i = [4,4,4,4,4,4,4]
# print(list_average (i))


# Returns a full name using first name and last name inputs
def full_name_generator(fname, lname):
    full = fname + lname
    return full

# f = input("First Name: ")
# l = input("Last Name: ")
# print(full_name_generator(f, l))
