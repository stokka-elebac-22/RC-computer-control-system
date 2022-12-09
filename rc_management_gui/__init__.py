"""__init__.py: Initialization class for the RC management GUI tool."""
__author__ = "Asbjørn Stokka"
__copyright__ = "Copyright 2022, ELEBAC"
__credits__ = ["Asbjørn Stokka"]
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Asbjørn Stokka"
__email__ = "asbjorn@maxit-as.com"
__status__ = "Testing"

from main_window_ui import Ui
import os
import argparse
from db_handler import *
from socket_client import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ELEBAC22 RC Computer interface.')
    parser.add_argument('--theme', dest='theme',
                        default='bachelor_car_menu_design',
                        help='name of theme file (default: bachelor_car_menu_design)')

    parser.add_argument('--fullscreen', dest='fullscreen',
                        default='false',
                        help='activate fullscreen mode (default: false)')

    parser.add_argument('--storage', dest='storage',
                        default='tmp_db.db', 
                        help='Choose SQLite storage (default: tmp_db.db)')

    args = parser.parse_args()
    if not (os.path.isfile(args.theme + '.ui')):
        print("Unable to locate the theme file, please check if it exists in the script folder")
        quit()
    if (args.fullscreen == "true" or args.fullscreen == "True"):
        fullscreen = True
    else:
        fullscreen = False
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"
    
    database = db_handler(args.storage)
    host = "10.0.10.95" #socket.gethostname()  # when both code is running on same pc
    port = 2004  # socket server port number    
    window = Ui(args.theme + '.ui', database, (host, port), fullscreen) 
    