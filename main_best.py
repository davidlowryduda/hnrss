#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run hnrss generator on HackerNews "Best" feed, with some simple logging.

Note that hnrss attempts to create an automated summary of the linked websites.
On atypical websites, this process can sometimes hang. So it is best practice
to run this with a time and memory management tool.

I currently use and recommend https://github.com/pshved/timeout
"""

from hnrss import *

import logging

LOG_FILENAME = 'logs/hnrss.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    format="%(asctime)s :: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")


logging.info("Beginning to perform 'best' RSS creation...")
HN_BEST = HNrss(HN_BEST_URL, title="Unofficial HackerNews best RSS")

logging.debug("Creating BEST RSS feed...")
try:
    HN_BEST.generate_feed()
    with open("bestrss.html", "w") as bestfile:
        bestfile.write(HN_BEST.feed.get_xml())
except Exception as e:
    logging.exception("Error occurred while creating BEST feed.")

logging.info("Ending RSS creation.")
