import pdb
import requests

class Card:
  def __init__(self, name, color, text):
    self.name = name
    self.color = color
    self.text = text


def parse_colors(color_array):
  color_string = ''
  colors = {
    "W": "White",
    "B": "Black",
    "U": "Blue",
    "R": "Red",
    "G": "Green"
  }
  for color_letter in color_array:
    color_string += colors[color_letter] + " "
  return color_string.strip()


BASE_URL = "https://api.magicthegathering.io/v1/cards"
query = input("Search for a card!\n")
request_url = f"{BASE_URL}?name={query}"
response = requests.get(request_url)
if response.status_code == 200:
  data = response.json()
  name = data["cards"][0]["name"]
  text = data["cards"][0]["text"]
  if "colors" in data["cards"][0]:
    colors = parse_colors(data['cards'][0]["colors"])
  else:
    colors = "Colorless"
  card1 = Card(name, colors, text)
else:
  print("Try a different Query value")

print(f"Card: {card1.name}\nColor(s): {card1.color}\nDescription: {card1.text}")
