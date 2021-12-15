import tkinter as tk

from pokechat import get_response, bot_name


"""UI for the PokeBot credits to Python Engineer @ https://www.youtube.com/watch?v=RNEcewpVZUQ"""
BG_GRAY_COLOR = '#37796C'
BG_COLOR = '#0C3348'
SEND_BUTTON_COLOR = '#E54222'
TEXT_COLOR = '#EAECEE'
FONT = "Helvetica 10"
FONT_BOLD = "Arial 14 bold"


class PokeBot(tk.Tk):
    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()

    def _setup_main_window(self):
        self.window.title("Chat with PokeBot")
        self.window.resizable(False, False)
        self.window.configure(width=570, height=650, bg=BG_GRAY_COLOR)
        self.window.config(padx=10, pady=10)

        # TITLE
        title_label = tk.Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="PokeBot",
                               font=FONT_BOLD, padx=10, pady=10)
        title_label.place(relwidth=1, relheight=0.1)

        # DIVIDER
        divider = tk.Label(self.window, width=450, bg=BG_GRAY_COLOR, height=2)
        divider.place(relwidth=1, relheight=0.01, relx=0, rely=0.07)

        # TEXT INPUT
        self.text_widget = tk.Text(self.window, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT,
                                   height=2, width=20, padx=5, pady=5)
        self.text_widget.place(relwidth=1, relheight=0.745, relx=0, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=tk.DISABLED)

        # SCROLLBAR
        scrollbar = tk.Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # BOTTOM LABEL
        bottom_label = tk.Label(self.window, bg=BG_GRAY_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # MESSAGE BOX
        self.msg_entry = tk.Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter)

        # SEND BUTTON
        send_button = tk.Button(bottom_label, text="Send", bg=SEND_BUTTON_COLOR, fg=TEXT_COLOR, font=FONT_BOLD,
                                width=20, command=lambda: self._on_enter(self.msg_entry.get()))
        send_button.place(relwidth=0.22, relheight=0.06, rely=0.008, relx=0.77)


    def _on_enter(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You: ")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, tk.END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg1)
        self.text_widget.configure(state=tk.DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg2)
        self.text_widget.configure(state=tk.DISABLED)

        self.text_widget.see(tk.END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    bot = PokeBot()
    bot.run()
