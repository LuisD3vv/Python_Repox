#Funciones puras e impuras

'''
a pure function is a function whose ouput solely from its
input values, without side effects

a impure function is a function that prints something to the terminal
this is the side effect
'''


'''
The Functional programming show us how to structuring code 
with functions offer a different approach when problem solving
'''

# Example 


# PURE solely returns the input and the operations no side effects
def calculate_circle_area(radio):
    return 3.1416 * pow(radio,2)

print(calculate_circle_area(10))

# IMPURE with the side effect

def calculate_circle_area(radio):
    result = 3.1416 * pow(radio,2)
    print(f"El area es {result}")
    return result

print(calculate_circle_area(10))