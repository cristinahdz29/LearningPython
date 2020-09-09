
# getting input from user in this case integers and adding together. this example contains integers and floats
# always have to put int function in front of variables when concatenating because input function always returns strings, which will not add but concatenate


# caclculate tip function

def calculate_tip(total_cost, percentage):
    return total_cost * (percentage/100)
    


tip = calculate_tip(100, 10)
print(tip)
