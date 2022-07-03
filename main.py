from manager.Manager import Manager
from modules.FluxRSS import FluxRSS
from modules.Instagram import Instagram
from modules.Youtube import Youtube


def main():
    m = Manager()
    m.register_module(
        Youtube({"url": "https://www.youtube.com/channel/UC2AEn2UpgLI0RDatPYZ3_gQ"})
    )
    m.register_module(
        Instagram({"url": "https://www.instagram.com/stephane_branly/?hl=fr"})
    )
    m.register_module(FluxRSS({"url": "https://www.lemonde.fr/sante/rss_full.xml"}))
    # m.get_modules()[1].render(m.get_device())
    m.get_modules()[0].render(m.get_device())
    m.get_modules()[1].render(m.get_device())
    # channel = yt.Youtube("https://www.youtube.com/channel/UC2AEn2UpgLI0RDatPYZ3_gQ")
    # leMonde = rss.fluxRSS("https://www.lemonde.fr/sante/rss_full.xml")
    # meteo = mt.Meteo("http://www.meteociel.fr/previsions/22572/hesdin_l_abbe.htm")
    # device.show_image(meteo.generateImage(),True)
    # p.wait(300)

    # game = mn.Manille((250,14,66),(34,230,150))
    # device.show_image(game.getImage())
    # while True:
    #     game.waitUpdate()
    #     game.animate(device)


if __name__ == "__main__":
    main()
