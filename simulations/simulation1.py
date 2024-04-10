class Chocolate:
    def __init__(self, weight, price, type, id):
        self.weight = weight
        self.price = price
        self.type = type
        self.id = id

# A distribution function to distribute chocolates to students
def distribute_chocolates(chocs, num_students):
    distribution = {f"Student {i+1}": [] for i in range(num_students)}
    for i, choc in enumerate(chocs):
        distribution[f"Student {(i % num_students) + 1}"].append(choc)
    return distribution

# A function to sort chocolates by weight
def sort_chocolates_by_weight(chocs):
    return sorted(chocs, key=lambda x: x.weight)

# A function to search chocolates by type
def search_chocolates_by_type(chocs, type_to_search):
    matches = [choc for choc in chocs if choc.type == type_to_search]
    if not matches:
        return f"No match found for '{type_to_search}'."
    return matches

# Display the distribution and search results
def display_distribution(distribution):
    for student, chocs in distribution.items():
        print(f"\n{student} received:")
        for choc in chocs:
            print(f"  - ID: {choc.id}, Type: {choc.type}, Weight: {choc.weight} gm, Price: {choc.price} AED")

def display_search_results(search_result):
    if isinstance(search_result, str):
        print(search_result)
    else:
        for choc in search_result:
            print(f"  - ID: {choc.id}, Type: {choc.type}, Weight: {choc.weight} gm, Price: {choc.price} AED")

# Setup for Simulation 1
chocolates_sim1 = [
    Chocolate(5, 2, "Almond chocolate", "002"),
    Chocolate(7, 4, "Peanut butter chocolate", "005"),
    Chocolate(3, 1, "Milk chocolate", "001"),
    Chocolate(6, 3, "Dark chocolate", "003"),
    Chocolate(4, 2.5, "White chocolate", "004")
]

# Distribute among 2 students
distribution_sim1 = distribute_chocolates(chocolates_sim1, 2)

# Sort chocolates for each student by weight and display
sorted_distribution_sim1 = {student: sort_chocolates_by_weight(chocs) for student, chocs in distribution_sim1.items()}

# Display distribution and sorting results
print("Simulation 1: Distribution and Sorting Results")
display_distribution(sorted_distribution_sim1)

# Search for "Almond chocolate" in each student's chocolates and display results
print("\nSimulation 1: Search Results")
for student in sorted_distribution_sim1:
    search_result = search_chocolates_by_type(sorted_distribution_sim1[student], "Almond chocolate")
    print(f"\nSearching for Almond chocolate in {student}'s chocolates:")
    display_search_results(search_result)
