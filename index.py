# console.log('Hello world!')
print('Hello world!')

# const whateverWeWant = "something"
# let whateverWeWant = "something"
# var whateverWeWant = "something"
whatever_we_want = "this is in python!"
print(whatever_we_want)

# WHATEVER = "this is hopefully a constant"
# print(WHATEVER)
# WHATEVER = "I hope this doesn't change but maybe it will"
# print(WHATEVER)
# we can change constants so they're not constant

# print(True)
# print(true) <--- this doesn't work!

# if (!true && true) {
#     console.log('this is true')
# } else {
#     console.log('this is false')
# }

# if not True and False:
#     print('I AM TRUE')
#     print('i will also run')
# else:
#     print('I AM FALSE')
#
# if (1 === "1") {
#     console.log("Definitely equal")
# } else {
#     console.log("Definitely NOT equal")
# }

# if 1 == '1':
#     print('I AM EQUAL')
# else:
#     print('I AM NOT EQUAL')

# if 1 != '1':
#     print('I AM NOT EQUAL')
# else:
#     print('I AM EQUAL')

# print('I AM TERNARY') if 1 == 1 else print('NO WAY')

# function myFunc() {
#     js in here
# }

# def my_func():
#     to_be_interpolated = "Hello!"
#     print(f"I am interpolated: {to_be_interpolated}")
#
# my_func()

# def empty_func():
#     pass
#
# empty_func()

# def with_args(arg1 = 1, arg2 = 2, arg3 = 3):
#     return f"{arg1} and {arg2} and {arg3}"
#
# print( with_args(arg2 = 9001) )

# const myArray = [1,2,3]
my_list = ['zero','one','two']

# const myObject = { one: 1, two: 2 }
my_dictionary = { 'one': 1, 'two': 2 }

# for key in my_dictionary:
#     print( my_dictionary[key] )

# print( my_dictionary['one'] )

# my_new_list = [val + " number" for val in my_list]

# my_new_list = [val + " is zero" if val == 'zero' else "not zero" for val in my_list]

# my_new_list = [val + " is zero" if val == 'zero' else "not zero" for val in my_list]

# my_new_list = [val + " is zero" for val in my_list if val == 'zero']

my_new_list = [val for val in my_list if val == 'zero']
# val = the value | for val is each val | in my_list is the list | if val is the conditonal

print( my_new_list )
