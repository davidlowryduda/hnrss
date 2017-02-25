#!/usr/bin/env python3
# encoding: utf-8

"""
Run hnrss generator on HackerNews "FrontPage" feed, with some simple logging.

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


logging.info("Beginning to perform RSS creation...")
HN_TOP = HNrss(HN_TOP_URL, title="Unofficial HackerNews frontpage RSS")

logging.debug("Creating TOP RSS feed...")
try:
    HN_TOP.generate_feed()
    with open("toprss.html", "w") as topfile:
        topfile.write(HN_TOP.feed.get_xml())
except Exception as e:
    logging.exception("Error occurred while creating TOP feed.")

logging.info("Ending RSS creation.")
