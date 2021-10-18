# write a normal function that accepts another function as an argument. Output the result of that other function in your normal function.
# Format the output of your 'normal' function such that numbers look nice and are centered in a 20 character column.
def normal_function(func, *arr):
   print('{:^20}'.format(func(arr)))

def get_max(arr):
   return max(arr)

normal_function(get_max, *[1,5,8,6])
# Call your normal function by passing a labda function - which performs any operation of your choice - as an argument
normal_function(lambda arr: min(arr), *[3,22,15,2])
# Tweak your normal function by allowing an infinite amount of arguments on which your labda function will be executed
normal_function(lambda arr: min(arr), 1,2,3,4,5,6,7,3,4,5,6)




