from data_package import remove_duplicates, strip_whitespaces, calculate_mean, find_maximum, find_minimum

def main():
    user_input = input ("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

    try:
        parts = user_input.split(",")
        cleaned = strip_whitespaces(parts)
        numbers = [float(f) for f in cleaned]
        unique_numbers = remove_duplicates(numbers)

        print(f"Cleaned and unique data: {unique_numbers}")
        print("-" * 30)
        print(f"Mean: {calculate_mean(unique_numbers)}")
        print(f"Maximum: {find_maximum(unique_numbers)}")
        print(f"Minimum: {find_minimum(unique_numbers)}")
    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")

if __name__ == "__main__":
    main()