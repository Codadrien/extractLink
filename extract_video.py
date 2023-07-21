from bs4 import BeautifulSoup
import json

html_file = "C:\\Users\\Adrien\\Desktop\\Dossier\\3 DEVELOPPEMENT\\Portfolio\\Script\\scrapVideo.html"

# Lire le contenu complet du fichier HTML
with open(html_file, "r") as file:
    html_content = file.read()

# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Trouver toutes les balises a avec la classe project-cover
cover_elements = soup.find_all("a", class_="project-cover")

# Créer une liste d'objets JSON pour chaque lien d'image
image_list = []
# Utiliser une variable compteur pour générer des identifiants uniques
counter = 1
for cover in cover_elements:
    image_link = cover.find("img", class_="cover__img")["src"]
    image_title = cover.find("div", class_="title").text.strip()
    image_obj = {"id": f"{counter}", "img": {"src": image_link, "title": image_title}}
    image_list.append(image_obj)
    counter += 1

# Créer le contenu JSON
json_data = json.dumps(image_list, indent=4)

# Écrire le contenu JSON dans un fichier
output_file = "C:\\Users\\Adrien\\Desktop\\Dossier\\3 DEVELOPPEMENT\\Portfolio\\Script\\dataVideo.json"
with open(output_file, "w") as file:
    file.write(json_data)

print("Le fichier JSON contenant les liens d'images a été enregistré dans", output_file)
