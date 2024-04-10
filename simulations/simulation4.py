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

def sort_chocolates_by_weight(chocs):
    return sorted(chocs, key=lambda x: x.weight)

# A function to search chocolates by type
def search_chocolates_by_type(chocs, type_to_search):
    matches = [choc for choc in chocs if choc.type == type_to_search]
    if not matches:
        return f"No match found for '{type_to_search}'."
    return matches

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

# Setup for Simulation 4
chocolates_sim4 = [
    Chocolate(5, 2, "Almond chocolate", "002"),
    Chocolate(7, 4, "Peanut butter chocolate", "005"),
    Chocolate(3, 1, "Milk chocolate", "001"),
    Chocolate(6, 3, "Dark chocolate", "003"),
    Chocolate(4, 2.5, "White chocolate", "004"),
    Chocolate(8, 5, "Mint chocolate", "006"),
    Chocolate(9, 6, "Berry chocolate", "009"),
    Chocolate(2, 1.5, "Hazelnut chocolate", "008"),
]

# Distribute among 5 students
distribution_sim4 = distribute_chocolates(chocolates_sim4, 5)

# No sorting is needed for this simulation as we're focusing on search functionality

# Conducting searches for specified types and displaying results
search_types = ["Milk chocolate", "Almond chocolate", "Berry chocolate", "Hazelnut chocolate"]
print("Simulation 4: Search Results")
for type_to_search in search_types:
    print(f"\nSearching for {type_to_search} across all students:")
    found = False
    for student in distribution_sim4:
        search_result = search_chocolates_by_type(distribution_sim4[student], type_to_search)
        if isinstance(search_result, list) and search_result:
            print(f"  Found in {student}'s chocolates:")
            display_search_results(search_result)
            found = True
    if not found:
        print(f"  No match found for '{type_to_search}' in any student's chocolates.")
