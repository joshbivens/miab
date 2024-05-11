# Programmer: Josh Bivens
# Email: thejoshbivens@gmail.com
# Purpose:
#   Entry point of the app.

import tkinter as tk
from MessageGUI import MessageInABottleGUI

if __name__ == "__main__":
    root = tk.Tk()
    gui = MessageInABottleGUI(root)
    gui.start()