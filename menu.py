from bs4 import BeautifulSoup
import requests



def Recevoir_menu():
    # Making a GET request
    r = requests.get(
        'http://cafe-battelle.eldora.ch/menus-du-jour/cafe-battelle/')

    html: str = r.text

    soup = BeautifulSoup(html, "html.parser")
    tuple_repas = [["lundi"], ["Mardi"], ["Mercredi"], ["Jeudi"], ["Vendredi"]]
    no_jour = -1

    for x in soup.find_all("div", attrs={'class': 'dayCover track'}):
        no_jour += 1
        # print(x,"\n\n")

        toto = BeautifulSoup(str(x), "html.parser")
        for y in toto.find_all("div", attrs={'class': 'col-md-5 col-sm-5 col-xs-10 col-xs-offset-1 menuPlat text-left'}):
            titi = BeautifulSoup(str(y), "html.parser")

            switch_menu_prix = 0
            for z in titi.find_all("p"):

                text: str = str(z)
                text = text.replace("<p>", "")
                text = text.replace('<p class="text-right menuPrix">', "")
                text = text.replace("<p", "")

                text = text.replace("</p>", "")
                text = text.replace('<br>', " ")
                text = text.replace('</br>', " ")
                text = text.replace('<br/>', " ")
                tuple_repas[no_jour].append(text)

            for y in toto.find_all("div", attrs={'class': 'col-md-5 col-sm-5 col-xs-10 col-xs-offset-1 menuPlat text-left col-md-offset-1 col-sm-offset-1'}):
                titi = BeautifulSoup(str(y), "html.parser")

                switch_menu_prix = 0
                for z in titi.find_all("p"):

                    text: str = str(z)
                    text = text.replace("<p>", "")
                    text = text.replace('<p class="text-right menuPrix">', "")
                    text = text.replace("<p", "")

                    text = text.replace("</p>", "")
                    text = text.replace('<br>', " ")
                    text = text.replace('</br>', " ")
                    text = text.replace('<br/>', " ")
                    tuple_repas[no_jour].append(text)
    return tuple_repas