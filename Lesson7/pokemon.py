import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import requests

# Maximum number of rows to display in output label
MAX_ROWS = 5

# Use https://docs.pokemontcg.io for details on data format.

def fetch_pokemon_data(pokemon_name):
    # Finds information on all pokemons with given name.
    # Returns a dictionary:
    #   data: array of dictionaries, one describing each pokemon
    url = f'https://api.pokemontcg.io/v2/cards?q=name:"{pokemon_name}"'
    response = requests.get(url)
    return response.json()


class Application(App):

    def __init__(self):
        super().__init__()
        self.pokemonData = {}

    def update_label(self):
        # Displays the information from self.pokemonData (list of dictionaries) in the output label.
        self.pokemonDataLabel.text = ''
        for pokemon in self.pokemonData[:MAX_ROWS]:
            self.pokemonDataLabel.text += f"{pokemon['name']} ({pokemon['set']['name']}) : {pokemon['hp']}HP\n"
        if len(self.pokemonData) > MAX_ROWS:
            self.pokemonDataLabel.text += '...'

    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.pokemonNameInput = TextInput(multiline=False)
        layout.add_widget(self.pokemonNameInput)
        
        self.fetchButton = Button(text="Fetch Pokemon Data", on_press=self.handle_click)
        layout.add_widget(self.fetchButton)

        self.pokemonDataLabel = Label(text="")
        layout.add_widget(self.pokemonDataLabel)

        return layout


    def handle_click(self, button):

        # Fetch data from API

        fetched_data = fetch_pokemon_data(self.pokemonNameInput.text)
        print('Fetched data: ', fetched_data)
  
        # Only update information if data is valid and nonempty.
        if fetched_data and 'data' in fetched_data.keys():
            self.pokemonData = fetched_data['data']
            self.update_label()



if __name__ == "__main__":
    myApp = Application()
    myApp.run()
