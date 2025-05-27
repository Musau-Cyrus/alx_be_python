weather = input(print("What's the weather like today (sunny/rainy/cold): ")).lower()

if weather == "sunny":
     print("Wear a tshirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget an umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure you wear a jacket and a scarf.")
else:
    print("Sorry! I don't have a recommendations for this weather.")
