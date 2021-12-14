import pypokedex
import tkinter as tk
import urllib3

from chat import get_response, bot_name
from io import BytesIO
from PIL import Image, ImageTk

BG_GRAY_COLOR = '#ABB2B9'
BG_COLOR = '#17202A'
TEXT_COLOR = '#EAECEE'

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 12 bold"


class PokeBot(tk.Tk):
    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()

        self.pokedex = pypokedex.Pokedex()

        self.text_input = tk.Text(self, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, height=1, width=50)
        self.text_input.pack(side=tk.BOTTOM, fill=tk.X)

        self.text_output = tk.Text(self, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, height=10, width=50)
        self.text_output.pack(side=tk.TOP, fill=tk.X)

        self.img_output = tk.Label(self, bg=BG_COLOR)
        self.img_output.pack(side=tk.TOP, fill=tk.X)

        self.text_input.bind("<Return>", self.on_enter)

        self.text_input.focus_set()


    def _setup_main_window(self):
        self.window.title("Chat with PokeBot")
        self.window.rezizable(False, False)
        self.window.configure(width=470, height=550, bg=BG_GRAY_COLOR)
        self.window.config(padx=10, pady=10)

        # TITLE
        title_label = tk.Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="PokeBot",
                              font=FONT_BOLD, padx=10, pady=10)
        title_label.place(relwidth=1, relheight=0.1)

        divider = Label(self.window, width=450, bg=BG_GRAY_COLOR, height=2)
        divider.place(relwidth=1, relheight=0.01, relx=0, rely=0.07)

        # TEXT INPUT
        self.text_widget = tk.Text(self.window, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, height=2, width=20)



    # Function to get the pokemon image
    def get_pokemon_image():
        # pypokedex.set_api_key("pkdx")
        # pypokedex.set_locale("en")
        pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
        sprite = pokemon.sprites.front.get("default")
        http = urllib3.PoolManager()
        response = http.request('GET', sprite)
        image = Image.open(BytesIO(response.data))

        img = ImageTk.PhotoImage(image)
        pokemon_image.config(image=img)
        pokemon_image.image = img

        pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
        pokemon_types.config(text="-".join([poke_type for poke_type in pokemon.types]).title())


        label_id_name = tk.Label(window, text="Pokemon  or Name:", font=("Arial", 20))
        label_id_name.pack(padx=10, pady=10)

        text_id_name = tk.Text(window, height=1, font=("Arial", 16))
        text_id_name.pack(padx=10, pady=10)

        btn_load = tk.Button(window, text="Load Pokemon", font=("Arial", 14), command=get_pokemon_image)
        btn_load.pack(padx=10, pady=10)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    bot = PokeBot()
    bot.run()
