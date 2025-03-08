import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import colorchooser
from colorama import init

# Initialize colorama
init(autoreset=True)

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

# GUI for the autoclicker
class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloodclicker v1")

        # Default background color
        self.bg_color = "#f0f0f0"  # Light gray background

        # Set the initial background color
        self.root.config(bg=self.bg_color)

        # Label
        self.label = tk.Label(root, text="Bloodclicker Settings", font=("Arial", 16), bg=self.bg_color)
        self.label.pack(pady=10)

        # CPS slider (Custom slider with circle handles)
        self.cps_label = tk.Label(root, text="Select CPS (clicks per second):", bg=self.bg_color)
        self.cps_label.pack(pady=5)

        self.slider_canvas = tk.Canvas(root, width=250, height=50, bg=self.bg_color, bd=0, highlightthickness=0)
        self.slider_canvas.pack(pady=5)

        # Draw slider line (for reference)
        self.slider_line = self.slider_canvas.create_line(25, 25, 225, 25, width=10, fill="gray")

        # Draw circle handle (initially set to the leftmost position)
        self.handle = self.slider_canvas.create_oval(20 - 10, 15, 20 + 10, 35, fill="black")  # Circle with radius 10

        # Set initial CPS value (handle starts at the leftmost point)
        self.current_cps = 1
        self.cps_slider_value = 1  # Default CPS value
        self.update_cps_label()

        # Bind mouse event for dragging the slider handle
        self.slider_canvas.bind("<B1-Motion>", self.on_drag)

        # Click type selection
        self.click_type_label = tk.Label(root, text="Select click type:", bg=self.bg_color)
        self.click_type_label.pack(pady=5)

        self.click_type_var = tk.StringVar()
        self.click_type_var.set("left")  # Default to left click

        self.left_click_rb = tk.Radiobutton(root, text="Left Click", variable=self.click_type_var, value="left", bg=self.bg_color)
        self.left_click_rb.pack(pady=3)

        self.right_click_rb = tk.Radiobutton(root, text="Right Click", variable=self.click_type_var, value="right", bg=self.bg_color)
        self.right_click_rb.pack(pady=3)

        self.both_click_rb = tk.Radiobutton(root, text="Both Clicks", variable=self.click_type_var, value="both", bg=self.bg_color)
        self.both_click_rb.pack(pady=3)

        # Background color change button
        self.bg_color_button = tk.Button(root, text="Change Background Color", command=self.change_bg_color, bg=self.bg_color)
        self.bg_color_button.pack(pady=10)

        # Start button
        self.start_button = tk.Button(root, text="Start Clicking", command=self.start_clicking, bg=self.bg_color)
        self.start_button.pack(pady=20)

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, bg=self.bg_color)
        self.exit_button.pack(pady=5)

    def update_cps_label(self):
        # Update the CPS label with the current value
        self.cps_label.config(text=f"Select CPS (clicks per second): {self.cps_slider_value}")

    def on_drag(self, event):
        # Update the handle position when dragging
        x_pos = event.x
        # Make sure the handle stays within the slider bounds
        if x_pos < 25:
            x_pos = 25
        elif x_pos > 225:
            x_pos = 225

        # Update handle position (move it horizontally)
        self.slider_canvas.coords(self.handle, x_pos - 10, 15, x_pos + 10, 35)

        # Update CPS value based on the position of the handle
        self.cps_slider_value = round((x_pos - 25) / 10) + 1
        self.update_cps_label()

    def change_bg_color(self):
        # Open color picker dialog
        color = colorchooser.askcolor()[1]
        if color:  # If a color is selected
            self.bg_color = color
            self.root.config(bg=self.bg_color)  # Change the background color of the root window
            # Update background color of widgets
            self.label.config(bg=self.bg_color)
            self.cps_label.config(bg=self.bg_color)
            self.click_type_label.config(bg=self.bg_color)
            self.left_click_rb.config(bg=self.bg_color)
            self.right_click_rb.config(bg=self.bg_color)
            self.both_click_rb.config(bg=self.bg_color)
            self.bg_color_button.config(bg=self.bg_color)
            self.start_button.config(bg=self.bg_color)
            self.exit_button.config(bg=self.bg_color)

            # Update slider background to match the window background color
            self.slider_canvas.config(bg=self.bg_color)  # Change the canvas background color

            # Update the slider line to blend with the background (keeping the gray color for visibility)
            self.slider_canvas.itemconfig(self.slider_line, fill="gray")

    def start_clicking(self):
        # Get CPS value from slider
        cps = self.cps_slider_value

        click_type = self.click_type_var.get()

        # Wait for 5 seconds before starting
        time.sleep(5)

        # Start clicking when 's' is pressed
        print(f"Starting clicker at {cps} CPS with {click_type} clicks...")
        click_at_cps(cps, click_type)

# Create the main window
root = tk.Tk()
app = AutoClickerApp(root)

# Run the GUI
root.mainloop()



