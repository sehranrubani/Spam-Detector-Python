# Rule Based Agents
  # Import required libraries
import re  # For using regular expressions to match patterns in text
import tkinter as tk  # For creating GUI elements
from tkinter import filedialog  # For opening file dialog to select files

# Define a list of spam keywords often found in spam messages
SPAM_KEYWORDS = [
    "free", "win", "winner", "congratulations", "urgent", "lottery", "claim prize",
    "click here", "limited time", "make money", "earn extra cash", "exclusive deal"
]

# Define suspicious spam patterns using regular expressions
SPAM_PATTERNS = [
    r'\b[A-Z]{5,}\b',  # Detects words in ALL CAPS with 5 or more letters (e.g., "URGENT")
    r'\b(?:https?://|www\.)\S+',  # Detects suspicious links (http, https, www)
    r'!{3,}',  # Detects excessive use of exclamation marks (e.g., "!!!")
]


def load_email():
    """
    Opens a file dialog for the user to select a .txt file containing email content.
    Reads the file and checks whether it is spam using the detect_spam() function.
    """
    # Open a file dialog and get the selected file's path
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not file_path:  # If no file is selected
        print("No file selected.")
        return

    # Open and read the content of the selected file
    with open(file_path, "r", encoding="utf-8") as file:
        email_content = file.read()

    # Check if the email content is spam
    is_spam = detect_spam(email_content)

    # Output result based on spam detection
    print("Spam Detected!" if is_spam else "Email is clean.")


def detect_spam(email_content):
    """
    Checks the given email content for spam by looking for predefined keywords and patterns.
    Returns True if any spam indicators are found; otherwise, returns False.
    """
    email_lower = email_content.lower()  # Convert to lowercase for keyword comparison

    # Look for any spam keyword in the content
    for keyword in SPAM_KEYWORDS:
        if keyword in email_lower:
            return True  # If found, it's spam

    # Look for any suspicious spam-like patterns
    for pattern in SPAM_PATTERNS:
        if re.search(pattern, email_content):
            return True  # If pattern matches, it's spam

    return False  # No spam detected


# Set up a basic GUI (hidden by default) to enable file selection dialog
root = tk.Tk()
root.withdraw()  # Hide the main tkinter window as we only need the file dialog

# Prompt user to select a file and begin the spam detection process
print("Select an email text file...")
load_email()