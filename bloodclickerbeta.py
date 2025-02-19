import pyautogui
import time
import keyboard
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Use raw string to avoid escape sequence warning
red_text = r"""
/$$$$$$$  /$$                           /$$           /$$ /$$           /$$
| $$__  $$| $$                          | $$          | $$|__/          | $$
| $$  \ $$| $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$$| $$ /$$  /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$
| $$$$$$$ | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____/| $$| $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$__  $$| $$| $$  \ $$| $$  \ $$| $$  | $$| $$      | $$| $$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
| $$  \ $$| $$| $$  | $$| $$  | $$| $$  | $$| $$      | $$| $$| $$      | $$_  $$ | $$_____/| $$
| $$$$$$$/| $$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$| $$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$
|_______/ |__/ \______/  \______/  \_______/ \_______/|__/|__/ \_______/|__/  \__/ \_______/|__/
"""

# Print the red text
print(Fore.RED + red_text)

# Function to perform clicking based on CPS and chosen click type
def click_at_cps(cps, click_type):
    click_interval = 1 / cps  # Calculate the time between each click
    last_click_time = time.perf_counter()

    while True:
        if keyboard.is_pressed('c'):  # Stop clicking when 'c' is pressed
            print("Stopping clicker...")
            break

        current_time = time.perf_counter()

        # If enough time has passed since the last click, perform the click
        if current_time - last_click_time >= click_interval:
            if click_type == "left":
                pyautogui.click(button='left')
            elif click_type == "right":
                pyautogui.click(button='right')
            elif click_type == "both":
                pyautogui.click(button='left')
                pyautogui.click(button='right')

            last_click_time = current_time  # Update the last click time

        # Minimal delay to avoid blocking the system
        time.sleep(0.001)  # Allow the system to yield control for smoother performance

# Ask the user to set the CPS with clear input
while True:
    try:
        print(Fore.WHITE + "\nEnter the CPS (clicks per second):", end=" ")  # Clean prompt, no extra newlines
        cps = int(input())  # Get CPS input from the user
        if cps <= 0:
            print(Fore.WHITE + "Please enter a positive integer for CPS.")
        else:
            break  # Exit loop if CPS is valid
    except ValueError:
        print(Fore.WHITE + "Invalid input! Please enter a valid integer.")

# Wait for 5 seconds before starting
time.sleep(5)

# Ask for click type preference
print(Fore.WHITE + "Choose click type: ")
print(Fore.WHITE + "1. Left Click")
print(Fore.WHITE + "2. Right Click")
print(Fore.WHITE + "3. Both Clicks")

while True:
    if keyboard.is_pressed('1'):  # Left Click
        click_type = "left"
        print(Fore.WHITE + "Left click mode selected.")
        break
    elif keyboard.is_pressed('2'):  # Right Click
        click_type = "right"
        print(Fore.WHITE + "Right click mode selected.")
        break
    elif keyboard.is_pressed('3'):  # Both Clicks
        click_type = "both"
        print(Fore.WHITE + "Both clicks mode selected.")
        break

# Start clicking when 's' is pressed
print(Fore.WHITE + "Press 's' to start clicking.")
while True:
    if keyboard.is_pressed('s'):  # Start clicking when 's' is pressed
        print(Fore.WHITE + f"Starting clicker at {cps} CPS with {click_type} clicks...")
        click_at_cps(cps, click_type)
        break







