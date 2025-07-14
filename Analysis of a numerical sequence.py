# Analysis of a numerical sequence
def analyze_sequence():
    print("=== Analysis of a numerical sequence ===")

    numbers = input("Enter your numbers separated by spaces: ").split()

    try:
        # Convert all values to floats
        num_list = [float(num) for num in numbers]

        if not num_list:
            print("Error: No numbers entered!")
            return

        # Calculate statistics
        print(f"\nResults:")
        print(f"Count: {len(num_list)}")
        print(f"Min: {min(num_list)}")
        print(f"Max: {max(num_list)}")
        print(f"Sum: {sum(num_list)}")
        print(f"Average: {sum(num_list) / len(num_list):.2f}")

    except ValueError:
        print("Error: Please enter only numbers separated by spaces!")


# Turn on
analyze_sequence()