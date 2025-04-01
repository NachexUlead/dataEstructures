import time
import sys
from colorama import init, Fore, Style

# initialize colorama for colors
init(autoreset=True)

messages = [
    "Loading daily tips... 💡",
    "Fetching inspiration for you... 🎨",
    "Bringing fresh ideas... 🚀",
    "Motivating your hustle... 💪",
    "Loading creativity... ✨",
    "Curating content for your scroll... 🔥",
]

# function to display the process with colors and style
def load_message(message, color=Fore.MAGENTA):
    for char in f"{color}[✔] {message}":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
    time.sleep(1)

print(Fore.CYAN + Style.BRIGHT + "📸 Preparing content for your feed...")

# Simulate message loading
for msg in messages:
    load_message(msg, Fore.YELLOW)

print(Fore.GREEN + Style.BRIGHT + "🎉 Happy debugged is running on your feed... 📸")
