from utils.agent import create_clevrr_agent, models
from utils.prompt import prompt

import argparse
from tkinter import *


def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Launch the application with optional model and UI settings.")
    
    # Add arguments
    parser.add_argument('--model', type=str, default='openai', choices=['openai', 'gemini'],
                        help="Choose the model to use. Default is 'openai'. Options: 'openai', 'gemini'.")
    parser.add_argument('--float-ui', type=int, default=1, choices=[0, 1],
                        help="Enable or disable the float UI. Default is 1 (enabled). Pass 0 to disable.")
    
    # Parse the arguments
    args = parser.parse_args()

    # Convert float-ui argument to boolean
    float_ui = bool(args.float_ui)

    # Print out the configurations
    print(f"Using model: {args.model}")
    print(f"Float UI is {'enabled' if float_ui else 'disabled'}")

    agent_executor = create_clevrr_agent(models[args.model], prompt)

    # GUI
    root = Tk()
    root.title("Clevrr Computer")
    
    BG_GRAY = "#5D5FEF"
    BG_COLOR = "#F2F2F2"
    TEXT_COLOR = "#1C1C1C"
    
    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"
    
    # Send function
    def send():
        send = "You -> " + e.get()
        txt.insert(END, "\n" + send)
    
        user = e.get().lower()
    
        if (user == "hello"):
            txt.insert(END, "\n" + "Bot -> Hi there, how can I help?", )
    
        elif (user == "exit"):
            txt.insert(END, "\n" + "Bot -> Have a nice day!")
    
        else:
            response = agent_executor.invoke({"input": user})
            txt.insert(END, "\n" + f"Bot -> {response.get('output')}")
    
        e.delete(0, END)
    
    
    lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to Clevrr Computer", font=FONT_BOLD, pady=10, width=40, height=2).grid(
        row=0)
    
    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)
    
    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)
    
    e = Entry(root, bg="#FCFCFC", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)
    
    send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                command=send).grid(row=2, column=1)

    root.attributes('-topmost', bool(args.float_ui))
    root.mainloop()

if __name__ == "__main__":
    main()