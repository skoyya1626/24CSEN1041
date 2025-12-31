def check_voting_eligibility(age):
    """
    Checks if a person is eligible to vote based on their age.

    Args:
        age (int): The age of the person.

    Returns:
        bool: True if eligible, False otherwise.
    """
    # The standard legal voting age in most places is 18
    legal_voting_age = 18

    if age >= legal_voting_age:
        return True
    else:
        return False

# --- Example Usage ---

# 1. Get input from the user
try:
    user_age_str = input("Please enter your age: ")
    user_age = int(user_age_str)

    # 2. Check eligibility using the function
    if check_voting_eligibility(user_age):
        print(f"You are {user_age} years old. You are eligible to vote.")
    else:
        # Calculate how many years are left until they can vote
        years_until_eligible = 18 - user_age
        print(f"You are {user_age} years old. You are not eligible to vote yet.")
        print(f"You will be eligible to vote in {years_until_eligible} year(s).")

except ValueError:
    print("Invalid input. Please enter a valid number for your age.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
output:Please enter your age: 20
You are 20 years old. You are eligible to vote
