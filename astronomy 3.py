import time

dust = 0
energy = 0
stage = 1

print("Welcome to the Star Life Cycle Game!")
time.sleep(2)
print("Press Enter to collect space dust.")
time.sleep(2)
print("Type e to gain energy.")
time.sleep(2)
print("Type q to quit.")

while True:
    print("\nStage:", stage)
    
    if stage == 1:
        print("You are a Nebula")
    if stage == 2:
        print("You are a Protostar")
    if stage == 3:
        print("You are a Main Sequence Star")
    if stage == 4:
        print("You are a Red Giant")
    if stage == 5:
        print("You are a White Dwarf")

    print("Dust:", dust)
    print("Energy:", energy)

    choice = input("What do you want to do? ")

    if choice == "q":
        print("Goodbye")
        break

    if choice == "e":
        energy = energy + 5
        print("You gained energy")

    dust = dust + 4

    if stage == 1 and dust >= 10 and energy >= 5:
        stage = 2
        print("You formed into a Protostar")

    if stage == 2 and dust >= 25 and energy >= 15:
        stage = 3
        print("You became a Main Sequence Star")

    if stage == 3 and dust >= 50 and energy >= 30:
        stage = 4
        print("You expanded into a Red Giant")

    if stage == 4 and dust >= 80 and energy >= 50:
        stage = 5
        print("You became a White Dwarf")
        print("Star life cycle complete")
        break
