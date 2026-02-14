import time

dust = 0
planets = {"small": 0, "medium": 0, "large": 0}
planets_cost = {"small": 3, "medium": 5, "large": 10}

print("Welcome to Planet Builder")
time.sleep(1.25)
print("Planet Builder helps you understand how planets are made by playing a simple and fun game.")
time.sleep(4)
print("Planets are born from cosmic dust swirling around stars.")
time.sleep(1.5)
print("Collect dust and build your own planets!")
time.sleep(2)
print("Press Enter to wait or type 's/m/l' to build a planet.\n")

while True:

    dustMultiplier = 1 + 0.5*planets["small"] + 1*planets["medium"] + 3*planets["large"]

    action = input("Action: ").lower()

    if action in ["s", "m", "l"]:
        size = {"s": "small", "m": "medium", "l": "large"}[action]
        cost = planets_cost[size]

        if dust >= cost:
            dust -= cost
            planets[size] += 1
            planets_cost[size] = int(cost * 1.5)
            print(size, "planet built!")
        else:
            print("Not enough dust!")

    dust += dustMultiplier

    print("\n---------------------------")
    print("Dust:", round(dust, 1))
    print("Dust Multiplier:", round(dustMultiplier, 1))
    print("---------------------------")
    print("Small Planets:", planets["small"])
    print("Medium Planets:", planets["medium"])
    print("Large Planets:", planets["large"])
    print("---------------------------")
    print("Next Costs:")
    print("Small:", planets_cost["small"])
    print("Medium:", planets_cost["medium"])
    print("Large:", planets_cost["large"])
    print("---------------------------")

    time.sleep(0.3)
