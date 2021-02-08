import Pixoo as p
import Youtube.youtube as yt
import FluxRSS.fluxRSS as rss
import Meteo.meteo as mt
import Manille.manille as mn

def main():
    device = p.Pixoo()
    device.connect()
    game = mn.Manille((250,14,66),(34,230,150))
    device.show_image(game.getImage())
    print("end")
    while True:

        game.waitUpdate()
        game.animate(device)
        # device.displayText("@stephane_branly : "+channel.subscribers+" abonnés",(120,20,20),(45,45,45),channel.defaultIcon())
        # device.displayText("Actu:"+leMonde.generateText(2),(170,00,235),(0,110,110),leMonde.defaultIcon())
main()