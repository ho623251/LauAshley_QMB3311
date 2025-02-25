# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name:Ashley Lau
#
# Date: 02/25/2025
# 
##################################################
#
# Sample Script for Midterm Examination: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for another script that would
# execute the scripts (to run the doctests)
# and imports the modules to test the functions.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

def CESutility(x, y, r):
    """
    Calculate the Constant Elasticity of Substitution (CES) utility function.

    Parameters:
    x (float): Quantity of good x consumed.
    y (float): Quantity of good y consumed.
    r (float): Substitution parameter, indicating the degree of complementarity or substitutability.

    Returns:
    float: Value of the CES utility function.
    """
    # Check the value of x 
    if x < 0:
        raise ValueError("x can't be negative")
    
    # Check the value of y 
    if y < 0:
        raise ValueError("y can't be negative")

    # Check the value of r 
    if r < 0:
        raise ValueError("r can't be negative")
    
    # Handle the special case where r = 0, which corresponds to Cobb-Douglas preferences
    if r == 0:
        return x * y

    # Compute the CES utility function for r ≠ 0
    utility = (x**r + y**r)**(1 / r)
    return utility


def CESutility_valid(x, y, r):
     """
     Augmented CES utility function that ensures valid input.
     param x: Quantity of good x consumed (must be non-negative)
     param y: Quantity of good y consumed (must be non-negative)
     param r: Substitution parameter (must be strictly positive)
     return: CES utility or None with error messages
    """
    
     if x < 0:
        print("Error: x must be non-negative")
        return None
     if y < 0:
        print("Error: y must be non-negative")
        return None

     if r <= 0:
        print("Error: r must be strictly positive.")
        
        return None
   
     return CESutility(x,y,r)


def CESutility_in_budget(x, y, r, px, py, w):

    if px < 0:
        print("Error: the price of x cannot be negative.")
        return None
    if py < 0:
        print("Error: the price of y cannot be negative.")
        return None
    if w < 0:
        print("Error: w (wealth) cannot be negative.")
        return None
    if r <= 0:
        print("Error: r must be strictly positive.")
        return None
    if px * x + py * y > w:
        print("Error: The chosen basket exceeds the budget.")
        return None
    
    return CESutility_valid(x, y, r)


#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 4
def max_CES_util(x_min, x_max , y_min, y_max, step, r , p_x, p_y , w ):
    
    

    if p_x * x_max + p_y * y_max > w:
        print("Error: The chosen basket exceeds the budget.")
        return None

    max_u = p_x * x_max + p_y * y_max

    return max_u


# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 

if __name__ == "__main__":
    doctest.testmod()

# Make sure to include examples in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 

    






##################################################
# End
##################################################
