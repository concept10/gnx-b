
import os
import sys
import re
import argparse
import subprocess
import time
import datetime
import json
import requests
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject, GLib

try:
    from gi.repository import Pango as pango
except:
        logging.error("Pango not found")
        sys.exit(1)

if __name__ == '__main__':
    GObject.threads_init()
    Gdk.threads_init()

    main = someApp()
    main.run()
    Gtk.main()
    
