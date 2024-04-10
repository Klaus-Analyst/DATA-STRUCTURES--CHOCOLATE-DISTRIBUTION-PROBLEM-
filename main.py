class Chocolate:
    def __init__(self, weight, price, type, id):
        self.weight = weight
        self.price = price
        self.type = type
        self.id = id

# List of chocolates (add more if you want)
chocolates = [
    Chocolate(5, 2, "Almond chocolate", "002"),
    Chocolate(7, 4, "Peanut butter chocolate", "005")
]

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
    return [choc for choc in chocs if choc.type == type_to_search]

# Example of distributing chocolates among 2 students
num_students = 2
distribution = distribute_chocolates(chocolates, num_students)

#show the distribution
print("Distribution of chocolates among students:")
for student, chocs in distribution.items():
    print(f"\n{student} received:")
    for choc in chocs:
        print(f"  - ID: {choc.id}, Type: {choc.type}, Weight: {choc.weight} gm, Price: {choc.price} AED")

# Sorting and searching within a student's chocolates
student_chocolates = distribution["Student 1"]
sorted_chocolates = sort_chocolates_by_weight(student_chocolates)
search_result = search_chocolates_by_type(student_chocolates, "Almond chocolate")

print("\nAfter sorting Student 1's chocolates by weight:")
for choc in sorted_chocolates:
    print(f"  - ID: {choc.id}, Type: {choc.type}, Weight: {choc.weight} gm, Price: {choc.price} AED")

print("\nSearching for Almond chocolate in Student 1's chocolates:")
for choc in search_result:
    print(f"  - ID: {choc.id}, Type: {choc.type}, Weight: {choc.weight} gm, Price: {choc.price} AED")
