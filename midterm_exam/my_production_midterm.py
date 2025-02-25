# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name:  Ashley Lau 
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

def total_revenue(units_sold: int, price: float):
    
    """
    Calculate the total revenue earned from selling a product.
    Preconditions: units_sold >= 0, price >= 0
    units_sold: The number of units sold (must be non-negative)
    price: The price per unit (must be non-negative)
    return: Total revenue
    
    >>> units_sold = 2 and price = 2
    >>> total = 4
    >>> units_sold = -2 and price = 3
    >>> The value of unit sold should not be negative
    
    """

    if units_sold < 0: 
        print("The value of unit sold should not be negative.")
    elif price < 0: 
        print("The value of price should not be negative.")
    else:
        total = units_sold * price
        
        return total

def total_cost(quantity_produced, fixed_cost, a):
    """
    Calculate the total cost incurred by a firm to produce a product.

    Parameters:
    quantity_produced (int or float): The number of units produced (q).
    fixed_cost (int or float): The fixed cost (b).
    a (int or float): The constant multiplied by the square of the number of units produced (a).

    Returns:
    float: Total cost incurred.

    >>> total_cost (2,2,2)
    >>> outcome 10
    >>> total_cost (-2,1,1)
    >>> outcome Quantity produced must be non-negative


    """
    if quantity_produced < 0:
        raise ValueError("Quantity produced must be non-negative.")
    elif fixed_cost < 0:
        raise ValueError("Fixed cost must be non-negative.")
    elif a < 0:
        raise ValueError("Constant 'a' must be non-negative.")
    else:
         return a * (quantity_produced ** 2) + fixed_cost


#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 1

def total_profit(num_units, unit_price, multiplier, fixed_cost) -> float:
    """ 
    num_units - number of units produced
    unit_price - price for each unit
    multiplier - constant multiplied by the square of the number of units produced
    fixed_cost - fixed cost 

    Examples 
    >>> total_profit(1,1,1,1)
    >>> profit = 1 - 2 = -1
    
    >>> total_profit(2,2,1,1)
    >>> profit = 4 - 5 = -1

    >>> total_profit(4,5,2,1)
    >>> profit = 20 -  33 = -13
    
    
    """

    revenue = num_units * unit_price
    cost = multiplier * (num_units ** 2) + fixed_cost
    profit = revenue - cost

    return profit

# Exercise 2
def max_profit_calc(unit_price, multiplier, fixed_cost) -> float:
    """ 
    unit_price - price for each unit
    multiplier - constant multiplied by the square of the number of units produced
    fixed_cost - fixed cost 

    Examples 
    >>> max_profit_calc(1,1,1)
    >>> 3/2
    
    >>> total_profit(2,2,1)
    >>> 3/2

    >>> total_profit(4,5,1)
    >>> 7/5
    
    
    """

    q = unit_price / (2 * multiplier) + fixed_cost

    if q > 0:
        q_max = q
    else:
        q_max = 0

    return q_max



# Exercise 3
def profit_max_q (q_max, step, unit_price, multiplier, fixed_cost):
    
    return None


# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


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
