# Programmer: Josh Bivens
# Email: thejoshbivens@gmail.com
# Purpose:
#   GUI class (and entry point) of the Message In A Bottle application. 
#   Creates/manages GUI components and interacts with the Message class 
#   to send and display messages. 


import tkinter as tk
from Message import Message

class MessageInABottleGUI:
    def __init__(self, window):
        self.called = False

        self.window = window
        window.title("Message In A Bottle - Bivens Final Project")
        window.geometry("400x305") # WxH
        window.configure(bg="#FCE8A4")

        # Create title label
        title_label = tk.Label(window, text="Message In A Bottle", font=("Papyrus", 26))
        title_label.pack(pady=(5, 0))
        title_label.configure(fg="#7c7148", bg="#FCE8A4")

        # Create subtitle label
        subtitle_label = tk.Label(window, text="Send a message, receive a message", font=("Garamond", 14))
        subtitle_label.pack(pady=(0, 5))
        subtitle_label.configure(fg="#7c7148", bg="#FCE8A4")

        # Create message display textbox
        self.message_display = tk.Text(window, width=70, height=10, wrap="word", font=("Verdana", 10))
        self.message_display.pack(padx=10)
        self.message_display.insert(tk.END, "It's oh so quiet...\n\n")

        # Create message entry widget
        self.message_entry = tk.Entry(window, font=("Verdana", 10))
        self.message_entry.pack(side=tk.LEFT, padx=10, pady=10, ipadx=10, expand=True, fill=tk.X)
        self.message_entry.focus()
        self.message_entry.bind('<Return>', self.set_message) # Binds the Enter key to the set_message method

        # Create send button
        send_button = tk.Button(window, text="Send", command=self.set_message)
        send_button.pack(side=tk.RIGHT, padx=(0, 10), pady=10, ipadx=5, ipady=2)

    def clear_prompt(self):
        self.message_display.delete(1.0, tk.END)

    def set_message(self): # event=None allows the method to be called by the Enter key
        # Clear prompt text after first message is sent
        if not self.called:
            self.clear_prompt()
            self.called = True
        
        self.get_message()
        user_input = self.message_entry.get()
        my_message = Message(user_input)
        my_message.post_to_firestore()
        self.message_entry.delete(0, tk.END)

    def get_message(self):
        self.message_display.tag_configure("underline", underline=True)
        try:
            random_message = Message.get_random_message()
            message = random_message[0]
            timestamp = random_message[1]
            self.message_display.insert(tk.END, timestamp + ":\n", "underline")
            self.message_display.insert(tk.END, message + "\n\n")
        except TypeError:
            self.message_display.insert(tk.END, "No messages in database.\n\n")
            
    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = MessageInABottleGUI(root)
    gui.start()
