from random import *
from tkinter import *
listaChamps = {1:"Aatrox",2:"Ahri",3:"Akali",4:"Akshan",5:"Alistar",6:"Amumu",7:"Anivia",8:"Annie",9:"Aphelios",10:"Ashe",11:"AurelionSol",12:"Azir",13:"Bard",15:"Blitzcrank",16:"Brand",17:"Braum",18:"Caitlyn",19:"Camille",20:"Cassiopeia",21:"Cho'Gath",22:"Corki",23:"Darius",24:"Diana",25:"Dr.Mundo",26:"Draven",27:"Ekko",28:"Elise",29:"Evelynn",30:"Ezreal",31:"Fiddlesticks",32:"Fiora",33:"Fizz",34:"Galio",35:"GangPlank",36:"Garen",37:"Gnar",38:"Gragas",39:"Graves",40:"Gwen",41:"Hecarim",42:"Heimerdinger",43:"Ilaoi",44:"Irelia",45:"Ivern",46:"Janna",47:"Jarvan IV",48:"Jax",49:"Jayce",50:"Jhin",51:"Jinx",52:"Kai'Sa",53:"Kalista",54:"Karma",55:"Karthus",56:"Kassadin",57:"Katarina",58:"Kayle",59:"Kayn",60:"Kennen",61:"Kha'Zix",62:"Kindred",63:"Kled",64:"Kog'Maw",65:"LeBlanc",66:"Lee Sin",67:"Leona",68:"Lillia",69:"Lissandra",70:"Lucian",71:"Lulu",72:"Lux",73:"Master Yi",74:"Malphite",75:"Malzahar",76:"Maokai",77:"Miss Fortune",78:"Mordekaiser",79:"Morgana",80:"Nami",81:"Nasus",82:"Nautilus",83:"Neeko",84:"Nidalee",85:"Nocturne",86:"Nunu",87:"Olaf",88:"Oriana",89:"Ornn",90:"Pantheon",91:"Poppy",92:"Pyke",93:"Qiyana",94:"Quinn",95:"Rakan",96:"Rammus",97:"Rek'Sai",98:"Rell",99:"Renekton",100:"Rengar",101:"Riven",102:"Rumble",103:"Ryze",104:"Samira",105:"Sejuani",106:"Senna",107:"Sett",108:"Shaco",109:"Shen",110:"Shyvana",111:"Singed",112:"Sion",113:"Sivir",114:"Skarner",115:"Sona",116:"Soraka",117:"Swain",118:"Syalas",119:"Syndra",120:"Tahm Kench",121:"Taliyah",122:"Talon",123:"Taric",124:"Teemo",125:"Thresh",126:"Tristana",127:"Trundle",128:"Tryndamere",129:"Twisted Fate",130:"Twitch",131:"Udyr",132:"Urgot",133:"Varus",134:"Vayne",135:"Veigar",136:"Vel'Koz",137:"Vi",138:"Victor",139:"Vladmir",140:"Volibear",141:"Warwick",142:"Wukong",143:"Xayah",144:"Xerath",145:"Xin Zhao",146:"Yasuo",147:"Yone",148:"Yorick",149:"Yuumi",150:"Zac",151:"Zed",152:"Ziggs",153:"Zilean",153:"Zoe",154:"Zyra"}
def clientE():
    def change():
        nombre = randint(1,155)
        champtxt.set(listaChamps.get(nombre))
    root = Tk()
    root.geometry("1400x700")#taille de la page
    root.title("Home")#titre de la page
    root.configure(bg="#69869C")#bg de la page

    Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
    Frame1.grid(column=2, row=1, padx=30, pady=30)
    champtxt = StringVar()
    champtxt.set('random')
    Label(Frame1, textvariable= champtxt).grid(column=2, row=0,pady = 50,padx=50)
    
    
    playb = PhotoImage(file = r"play.png")#image
    Bouton1=Button(root,image = playb, command= change,bg="#69869C")#boutton avec une comande et un text à l'interrieur
    Bouton1.grid(column=1, row=1,pady = 50,padx=50)#positionnement des élements

    Fonction1 = Label(root, text = "random champ",bg="#69869C",)
    Fonction1.config(font=("Arial", 20))
    Fonction1.grid(column=1, row=2,pady = 0,padx=50)
    root.mainloop()

clientE()