import Pixoo as p
import Youtube.youtube as yt

def main():
    device = p.Pixoo()
    device.connect()
    device.displayText("Bonjour !")
    channel = yt.Youtube("https://www.youtube.com/channel/UC2AEn2UpgLI0RDatPYZ3_gQ")
    channel.check_views()
    device.displayText("@stephane_branly : "+channel.subscribers+" abonnés")
main()