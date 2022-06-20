#!/usr/bin/python3


def safe_print_division(a, b):
    
    try:
        num_div = a / b
    except (TypeError, ZeroDivisionError):
        num_div = None
    finally:
        print("Inside result: {}".format(num_div))
    return num_div