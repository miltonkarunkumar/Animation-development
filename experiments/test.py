import math
import easingfunctions  # Import your easing functions module

# A dictionary to map function names to the actual function objects
easing_functions = {
    "linear": easingfunctions.linear,
    "easeInSine": easingfunctions.easeInSine,
    "easeOutSine": easingfunctions.easeOutSine,
    "easeInOutSine": easingfunctions.easeInOutSine,
    "easeInQuad": easingfunctions.easeInQuad,
    "easeOutQuad": easingfunctions.easeOutQuad,
    "easeInOutQuad": easingfunctions.easeInOutQuad,
    "easeInCubic": easingfunctions.easeInCubic,
    "easeOutCubic": easingfunctions.easeOutCubic,
    "easeInOutCubic": easingfunctions.easeInOutCubic,
    "easeInQuart": easingfunctions.easeInQuart,
    "easeOutQuart": easingfunctions.easeOutQuart,
    "easeInOutQuart": easingfunctions.easeInOutQuart,
    "easeInQuint": easingfunctions.easeInQuint,
    "easeOutQuint": easingfunctions.easeOutQuint,
    "easeInOutQuint": easingfunctions.easeInOutQuint,
    "easeInExpo": easingfunctions.easeInExpo,
    "easeOutExpo": easingfunctions.easeOutExpo,
    "easeInOutExpo": easingfunctions.easeInOutExpo,
    "easeInCirc": easingfunctions.easeInCirc,
    "easeOutCirc": easingfunctions.easeOutCirc,
    "easeInOutCirc": easingfunctions.easeInOutCirc
}

def main():
    print("Available easing functions:")
    for func_name in easing_functions.keys():
        print(func_name)

    selected_function = input("Select an easing function: ")

    # Check if the selected function is valid
    if selected_function in easing_functions:
        t = float(input("Enter a value for t (between 0 and 1): "))
        if 0 <= t <= 1:
            result = easing_functions[selected_function](t)
            print(f"The result of {selected_function} at t={t} is {result}")
        else:
            print("Invalid value for t. It should be between 0 and 1.")
    else:
        print("Invalid function name. Please select a valid easing function.")

if __name__ == "__main__":
    main()
