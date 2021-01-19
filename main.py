import Pixoo as p
import Youtube.youtube as yt
import FluxRSS.fluxRSS as rss

def main():
    device = p.Pixoo()
    device.connect()
    # device.displayText("Bonjour !")
    channel = yt.Youtube("https://www.youtube.com/channel/UC2AEn2UpgLI0RDatPYZ3_gQ")
    leMonde = rss.fluxRSS("https://www.lemonde.fr/rss/une.xml")
    while True:
        channel.check_views()
        leMonde.updateNews()
        device.displayText("@stephane_branly : "+channel.subscribers+" abonnés",(190,10,10),channel.defaultIcon())
        device.displayText("Actu:"+leMonde.generateText(2),(190,10,255),leMonde.defaultIcon())
main()