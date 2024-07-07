# Dictionary

chai_types = { "Masala" : "Spicy", "Ginger" : "Zesty", "Green" : "Mild" }

chai_types["Green"]  = "Fresh"

for chai in chai_types:
    print(chai, chai_types[chai])


for key, value in chai_types.items():
    print(key, value)

tea_shop = {
    "chai" : {
        "Masala" : "Spicy",
        "Ginger" : "Zesty"
    },
    "tea" : {
        "Green" : "Mild",
        "Black" : "Strong"
    }
}

print(tea_shop["chai"]["Masala"])

squared_num = {x: x**2 for x in range(6)}


squared_num.clear()

print(squared_num)

keys = ["Masala", "Ginger", "Lemon"]

default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)

print(new_dict)
