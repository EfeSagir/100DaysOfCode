student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

print(capitals.get("France"))
capitals.update({"Turkey": "Ankara"})
print(capitals)
capitals.pop("Germany")
capitals.popitem()
capitals.clear
keys = capitals.keys()
print(keys)
values = capitals.values()
print(values)
items = capitals.items()
print(items)

for key,value in items:
    print(f"{key} : {value}")

travel_log = {
    "France": ["Paris", "Lille", "Dij"],
    "Germany": ["Stuttgart", "Berlin"]
}

# print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "num_times_visited": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "num_times_visited": 5
    }
}

print(travel_log["Germany"]["cities_visited"][2])

operator = input("pls enter operator")

if isinstance(operator, str):
    print(operator)

Dictionary = {"Key" : "Value"}

programming_dictionary = {"Bug" : "An error in a program that prevents the program from running as expected.",
                          "Function" : "A piece of code that you can easily call over and over again.",
                          "Loop" : "The action of doing something of doing over and over again.",
                          123 : "It is a combination of the first 3 positive numbers"}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])
print(programming_dictionary[123])
programming_dictionary["Continue"] = "It is a control flow statament for loops to whether you want to skip execution of a specific part in your code."
print(programming_dictionary["Continue"])

empty_dictionary = {}
print(empty_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary)

# nesting is adding a item into a dictionary

Dictionary = {"Key" : "Value 1",
              "Key 2" : "Value 2"}

capitals = {"Germany" : "Berlin",
            "France" : "Paris",
            "Turkey" : "Ankara"} 	#Lists can be indexed directly (e.g., nested_list[2][0]), while Dictionaries require keys to access values (e.g., capitals["Germany"]).


print(capitals["France"][1])

travel_log = {
    "France": {
        "num_times_visited": 9,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}


print(travel_log["Germany"]["cities_visited"][2])

name = input("Please enter your name:\n")
bid = input("Please enter your bid:\n")

bidding_dictionary = {}
bidding_dictionary[name] = bid

yes_or_no = input("If you want to enter another input write Y if you don't write N.")
while True:
    if (yes_or_no == "Y"):
        print("\n" * 100)
        name = input("Please enter your name:\n")
        bid = input("Please enter your bid:\n")
        bidding_dictionary[name] = bid
        yes_or_no = input("If you want to enter another input write Y if you don't write N.")

    elif(yes_or_no == "N"):
        max_bidding = max(bidding_dictionary.values())
        print(f"The highest bid is {bidding_dictionary[max_bidding]} by {max_bidding}")
        break