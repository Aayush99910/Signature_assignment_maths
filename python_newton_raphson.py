import math

def newton_raphson_method(x_value_guess):
    points_for_graph = [] # list which will store the coordinates
    tolerance_for_right_answer = 1e-6

    while (True):
        function_x = x_value_guess**2 + math.exp(x_value_guess) - 4 # f(x) is x^2 + e^x - 4
        first_derivate_function_x = 2 * x_value_guess + math.exp(x_value_guess) # f'(x) is 2x + e^x

        # here x(n+1) is next guess value which is stored in variable next_value_of_x
        # x(n) i current guess value which is stored in variable x_value_guess
        # f(xn) is the function value of x(n) stored in function_x variable
        # f'(xn) is the function value of first derivative of f(xn) which is stored in first_derivate_function_x
        next_value_of_x = x_value_guess - function_x / first_derivate_function_x # this is because x(n + 1) = xn - f(xn) / f'(xn)

        points_for_graph.append({'x': x_value_guess, 'y': function_x})
        
        if (abs(next_value_of_x - x_value_guess) < tolerance_for_right_answer):
            return x_value_guess, points_for_graph
        
        x_value_guess = next_value_of_x


def main():
    root_approximate_1, points_1 = newton_raphson_method(1)
    root_approximate_2, points_2 = newton_raphson_method(-2)  # Initial guess for the second root
    
    print("x", "y")
    for point in points_1:
        x = point['x']
        y = point['y']
        print(f"{x} {y}")
    print(f"Root approximate 1 of function x^2 + e^x - 4 is {root_approximate_1}.")
    
    print("\nx", "y")
    for point in points_2:
        x = point['x']
        y = point['y']
        print(f"{x} {y}")
    print(f"Root approximate 2 of function x^2 + e^x - 4 is {root_approximate_2}.")

main()