import geometry_utils

def main():
    operations = {
        "circle_area":
            (geometry_utils.circle_area, ["radius"]),
        "circle_perimeter":
            (geometry_utils.circle_perimeter, ["radius"]),
        "rectangle_area":
            (geometry_utils.rectangle_area, ["width", "height"]),
        "rectangle_perimeter":
            (geometry_utils.rectangle_perimeter, ["width", "height"]),
        "triangle_area":
            (geometry_utils.triangle_area, ["base", "height"])
    }

    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")
    operation = input("Enter the operation you want to perform: ").strip()

    if operation not in operations:
        print("Invalid operation.")
        return

    func, params = operations[operation]

    try:
        values = [float(input(f"Enter {p}: ")) for p in params]
        result = func(*values)
        print(f"Result: {result:.2f}")
    except ValueError as e:
        message = str(e)
        if "could not convert" in message:
            print("Input Error: Please enter valid numeric values.")
        else:
            print(f"Input Error: {message}")

if __name__ == "__main__":
    main()