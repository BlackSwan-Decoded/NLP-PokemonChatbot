from io import BytesIO
from PIL import Image, ImageTk
import pypokedex
import tkinter as tk
import urllib3

window = tk.Tk()
window.title("PokeBot")
window.geometry("400x400")
window.config(background='#000000')
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="PokeBot", font=("Arial", 32), bg='#000000', fg='#ffffff')
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window, font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)


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

window.mainloop()
