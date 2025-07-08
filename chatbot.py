import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Define chatbot responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"how are you ?", ["I'm good, thanks! How about you?", "Doing great. Hope you're well too!"]],
    [r"i am fine|i am good", ["That's great to hear!", "Awesome!"]],
    [r"what is your name ?", ["I'm ChatBuddy, your Python chatbot!"]],
    [r"who created you ?", ["A Python programmer like you!"]],
    [r"what can you do ?", ["I can chat with you and answer basic questions."]],
    [r"tell me a joke", ["Why did the computer go to the doctor? Because it had a virus!"]],
    [r"thank you|thanks", ["You're welcome!", "Glad I could help!"]],
    [r"bye|exit|quit", ["Goodbye! Have a great day!", "See you soon!"]],
    [r"(.*)", ["Interesting... tell me more!", "Hmm, I didn't get that. Can you rephrase?"]]
]

# Create chatbot object
chatbot = Chat(pairs, reflections)

# Function to get timestamp
def get_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# Send message and get response
def send_message():
    user_input = entry_box.get()
    if user_input.strip() == "":
        return

    user_time = get_timestamp()
    bot_response = chatbot.respond(user_input)
    bot_time = get_timestamp()

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You {user_time}:\n{user_input}\n", "user")
    chat_log.insert(tk.END, f"Bot {bot_time}:\n{bot_response}\n\n", "bot")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
    entry_box.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("ChatBuddy - Your Python Chatbot")

# Chat log
chat_log = scrolledtext.ScrolledText(root, state=tk.DISABLED, width=70, height=20, wrap=tk.WORD, font=("Arial", 11))
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entry box
entry_box = tk.Entry(root, width=60, font=("Arial", 12))
entry_box.grid(row=1, column=0, padx=10, pady=5)
entry_box.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(root, text="Send", width=10, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=5)

# Style tags (optional: make text more readable)
chat_log.tag_config("user", foreground="blue")
chat_log.tag_config("bot", foreground="green")

# Start GUI loop
root.mainloop()