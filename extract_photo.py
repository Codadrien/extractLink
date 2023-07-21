from bs4 import BeautifulSoup
import json

html_file = "C:\\Users\\Adrien\\Desktop\\Dossier\\3 DEVELOPPEMENT\\Portfolio\\Script\\scrapPhoto.html"

# Lire le contenu complet du fichier HTML
with open(html_file, "r") as file:
    html_content = file.read()

# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Trouver toutes les balises img avec la classe grid__item-image
image_elements = soup.find_all("img", class_="grid__item-image")

# Créer une liste d'objets JSON pour chaque lien d'image
image_list = []
counter = 1
for img in image_elements:
    image_link = img["src"]
    image_obj = {"id": f"{counter}","img": {"src": image_link}}
    image_list.append(image_obj)
    counter += 1

# Créer le contenu JSON
json_data = json.dumps(image_list, indent=4)

# Écrire le contenu JSON dans un fichier
output_file = "C:\\Users\\Adrien\\Desktop\\Dossier\\3 DEVELOPPEMENT\\Portfolio\\Script\\dataPhoto.json"
with open(output_file, "w") as file:
    file.write(json_data)

print("Le fichier JSON contenant les liens d'images a été enregistré dans", output_file)
