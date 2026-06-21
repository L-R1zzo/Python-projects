def square_root_bisection(x, tolerance=0.01, max_iterations=1000):
    if x < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif x == 0 or x == 1:
        print(f"The square root of {x} is {x}")
        return x
    else:
        if x < 1:
            high = 1
            low = x**2
        else:
            high = x
            low = 0
        interations = 0
        mid = (high + low) / 2

        while abs(mid**2-x) > tolerance and (high-low)/2:
            mid = (high + low) / 2
            interations += 1
            if interations == max_iterations:
                print(f"Failed to converge within {max_iterations} iterations")
                return None
            if mid**2 > x:
                high = mid
            elif mid**2 < x:
                low = mid 

        print(f"The square root of {x} is approximately {mid}")
        return mid    
    
square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(0.25, 1e-7, 50)
