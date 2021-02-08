import Pixoo as p
import Youtube.youtube as yt
import FluxRSS.fluxRSS as rss
import Meteo.meteo as mt
import Manille.manille as mn

def main():
    device = p.Pixoo()
    device.connect()

    channel = yt.Youtube("https://www.youtube.com/channel/UC2AEn2UpgLI0RDatPYZ3_gQ")
    leMonde = rss.fluxRSS("https://www.lemonde.fr/sante/rss_full.xml")
    device.displayText("@stephane_branly : "+str(channel.subscribers)+" abonnés",(120,20,20),(45,45,45),channel.defaultIcon())
    device.displayText("Actu:"+leMonde.generateText(3),(170,00,235),(0,110,110),leMonde.defaultIcon())


    game = mn.Manille((250,14,66),(34,230,150))
    device.show_image(game.getImage())
    while True:
        game.waitUpdate()
        game.animate(device)
main()