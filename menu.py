from bs4 import BeautifulSoup
import requests



def Recevoir_menu():
    # Récuperation des données sur le serveur
    r = requests.get(
        'http://cafe-battelle.eldora.ch/menus-du-jour/cafe-battelle/')
    #recupération du code html/css/js
    html: str = r.text
    #mise du html dans un objet soup afin de la manipuler 
    soup = BeautifulSoup(html, "html.parser")
    #tuple qui contiendra les menus de la semaine
    tuple_repas = [["lundi"], ["Mardi"], ["Mercredi"], ["Jeudi"], ["Vendredi"]]
    no_jour = -1
    #pour chaque div ayant pour class "dayCover track", est egual a chaque jour
    for x in soup.find_all("div", attrs={'class': 'dayCover track'}):
        no_jour += 1
        #retransforme le code correspondant au jour en objet beautifull soup
        toto = BeautifulSoup(str(x), "html.parser")
        #pour chaque div ayant comme class ""
        for y in toto.find_all("div", attrs={'class': 'col-md-5 col-sm-5 col-xs-10 col-xs-offset-1 menuPlat text-left'}):
            ##retransforme le code correspondant a un repas du jour en objet soupe

            titi = BeautifulSoup(str(y), "html.parser")

            #passe en revu le contenu des  balise p
            for z in titi.find_all("p"):

                text: str = str(z)
                #enleve les restant de code html
                text = text.replace("<p>", "")
                text = text.replace('<p class="text-right menuPrix">', "")
                text = text.replace("<p", "")

                text = text.replace("</p>", "")
                text = text.replace('<br>', " ")
                text = text.replace('</br>', " ")
                text = text.replace('<br/>', " ")
                #ajoute au repas du jour
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