# Function to determine the division based on the rating
def find_division(rating):
    if rating >= 1900:
        return "Division 1"
    elif rating >= 1600:
        return "Division 2"
    elif rating >= 1400:
        return "Division 3"
    else:
        return "Division 4"

# Number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    rating = int(input())
    division = find_division(rating)
    print(division)
