import numpy as np

def find_term_derivative(term):
    constant = term[0]*term[1]
    exponent = term[1] - 1
    return (constant, exponent)

def find_derivative(function_terms):
    derivative_terms = list(map(lambda term: find_term_derivative(term),function_terms))
    return list(filter(lambda derivative_term: derivative_term[0] != 0, derivative_terms))

def term_output(term, input_value):
    return term[0]*input_value**term[1]

def output_at(list_of_terms, x_value):
    outputs = list(map(lambda term: term_output(term, x_value), list_of_terms))
    return sum(outputs)

def derivative_at(terms, x):
    derivative_fn = find_derivative(terms)
    total = 0
    for term in derivative_fn:
        total += term[0]*x**term[1]
    return total

tuple_sq_pos  = np.array([[2, 2], [-8, 1]])
print(tuple_sq_pos)
# x_values = np.linspace(-6, 10, 100)
x_values = list(range(1,4))
print(x_values)
function_values = list(map(lambda x: output_at(tuple_sq_pos, x), x_values))

derivative_values = list(map(lambda x: derivative_at(tuple_sq_pos, x),x_values))

print(function_values)
print(derivative_values)

# import matplotlib.pyplot as plt
# # %matplotlib inline

# fig, ax = plt.subplots(figsize=(12,5))

# # plot 1
# plt.subplot(121)
# plt.axhline(y=0, color='lightgrey', )
# plt.axvline(x=0, color='lightgrey')
# plt.plot(x_values, function_values, label = "f (x) = 2x^2−8x ")

# plt.legend(loc="upper left", bbox_to_anchor=[0, 1], ncol=2, fancybox=True)

# # plot 2
# plt.subplot(122)
# plt.axhline(y=0, color='lightgrey')
# plt.axvline(x=0, color='lightgrey')
# plt.plot(x_values, derivative_values,color="darkorange", label = "f '(x) = 4x-8")

# ax.grid(True, which='both')

# plt.legend(loc="upper left")
# plt.show()