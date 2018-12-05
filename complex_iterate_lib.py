"""
Problem Set 8 Complex Number Iterations
NAME : {Xander Dressler}

complete the code for the functions below


"""
import os
def do_calculation(complex_num, complex_seed):
    """
    Takes two inputs, complex_num which is a complex number and
    a seed which is also a complex numberself.
    The calculation will square the complex number and then
    add the seed to it.

    Then return the new complex number
    """
    result = (complex_num **2) + complex_seed
    #print(result)
    return result
def do_iteration(complex_num, complex_seed):
    """
    Takes two inputs, a complex number and a seed which is also
    a complex numberself.
    You have made the do_calculation function above.  Use that here.
    We will do a calculation on the complex number and seed.
    Then take the resulting complex number as the new complex number and
    then do the calculation again with that new complex number and the same
    original seed.
    Keep doing this until EITHER
    (a) the new complex number get more than 2 "units" away from the origin
    OR
    (b) you have iterated 255 times

    When this has completed, return the number of iterations that executed
    """
    x = complex_num
    for i in range(255):
        ans = do_calculation(x, complex_seed)
    #    print(ans)
        x = ans
        if abs(x) > 2:
            print("MAX Epicness")
            break
    print(i)
    return i + 1
