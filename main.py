import Pixoo as p
import Youtube.youtube as yt
import FluxRSS.fluxRSS as rss
import Meteo.meteo as mt

def main():
    # device = p.Pixoo()
    # device.connect()
    # device.displayText("Bonjour !")
    channel = yt.Youtube("https://www.youtube.com/channel/UC2AEn2UpgLI0RDatPYZ3_gQ")
    leMonde = rss.fluxRSS("https://www.lemonde.fr/rss/une.xml")
    meteo = mt.Meteo("http://www.meteociel.fr/previsions/22572/hesdin_l_abbe.htm")
    meteo.update()
    print("end")
    while False:
        channel.check_views()
        leMonde.updateNews()
        # device.show_image(meteo.getMeteoImage())
        # device.displayText("@stephane_branly : "+channel.subscribers+" abonnés",(120,20,20),(45,45,45),channel.defaultIcon())
        # device.displayText("Actu:"+leMonde.generateText(2),(170,00,235),(0,110,110),leMonde.defaultIcon())
main()