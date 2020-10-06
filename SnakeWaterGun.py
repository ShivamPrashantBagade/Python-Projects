import random

print("")
print("Lets play snake water gun!!!")
print("")
print("""Snake:s  Gun:g  Water:w""")

draw_count = 0
cpu_win_count = 0
player_win_count = 0

turns = 0
while turns < 5:

    user_input = input("Choose from snake,water and gun : ")

    if user_input == "s" or user_input == "w" or user_input == "g":
        pass
    else:
        print("Entered Valid input")
        exit()

    choice_list = ["s", "w", "g"]

    cpu_input = random.choice(choice_list)

    # Draw cases
    if user_input == "s" and cpu_input == "s":
        print(f"Game is draw as both selected {user_input}")
        draw_count += 1

    if user_input == "w" and cpu_input == "w":
        print(f"Game is draw as both selected {user_input}")
        draw_count += 1

    if user_input == "g" and cpu_input == "g":
        print(f"Game is draw as both selected {user_input}")
        draw_count += 1

    # Player wins
    if user_input == "w" and cpu_input == "g":
        print(f"Player wins as cpu selected {cpu_input}")
        player_win_count += 1

    if user_input == "s" and cpu_input == "w":
        print(f"Player wins as cpu selected {cpu_input}")
        player_win_count += 1

    if user_input == "g" and cpu_input == "s":
        print(f"Player wins as cpu selected {cpu_input}")
        player_win_count += 1

    # Cpu wins
    if user_input == "g" and cpu_input == "w":
        print(f"Cpu wins as cpu selected {cpu_input}")
        cpu_win_count += 1

    if user_input == "s" and cpu_input == "g":
        print(f"Cpu wins as cpu selected {cpu_input}")
        cpu_win_count += 1

    if user_input == "w" and cpu_input == "s":
        print(f"Cpu wins as cpu selected {cpu_input}")
        cpu_win_count += 1

    turns += 1

if __name__ == "__main__":

    print("")
    print(f"Player Points {player_win_count}")
    print("")
    print(f"Cpu Points {cpu_win_count}")
    print("")
    print(f"Number of draw are {draw_count}")
