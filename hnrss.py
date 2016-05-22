#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creates an RSS feed from HackerNews because there isn't a good one out there.
"""

from urllib.request import urlopen
import feedmaker as rss2feed
import json
import time

# From the HN API
HN_API_BASE_URL = "https://hacker-news.firebaseio.com/v0/"
HN_BEST_URL = HN_API_BASE_URL + "beststories.json"
HN_TOP_URL = HN_API_BASE_URL + "topstories.json"
HN_NEW_URL = HN_API_BASE_URL + "newstories.json"


class HNrss(object):
    "Create RSS feed for HackerNews"

    def __init__(self,
                 api,
                 link="https://news.ycombinator.com",
                 numposts=10):
                 #title="Unofficial HackerNews RSS",
                 #description="A work in progress",
        self.title = "Unofficial HackerNews RSS."
        self.link = link
        self.description = ("Created and maintained by David Lowry-Duda "
                            "<davidlowryduda@davidlowryduda.com> "
                            "davidlowryduda.com")
        self.api = api
        self.numposts = numposts
        self.xml = ""

        self.feed = rss2feed.FeedMaker(title=self.title,
                                       link=self.link,
                                       description=self.description)

    def generate_feed(self):
        "Fills the rss feed with `numpost` posts, each with at most 5 comments."
        post_ids = self._get_post_ids(self.api)
        # Now have a list of 50 post ids.
        for pid in post_ids:
            post_data = self._get_post_data(pid)
            post_title = post_data.get('title', "")
            post_score = post_data.get('score', "")
            post_author = post_data.get('by', "")
            post_kids = post_data.get('kids', "")
            post_time = self._format_time(post_data.get('time'))
            post_url = post_data.get('url', "")
            post_text = post_data.get('text', "")

            post_text += ("<p>Current post score: {}. "
                          "Full comments are at "
                          "https://news.ycombinator.com/item?id={}</p>"
                          ).format(post_score, pid)

            if post_kids:
                post_text += ("<h3> Top Comments </h3><ol>\n\n")

            for kid in post_kids[:5]:
                kid_data = self._get_post_data(kid)
                kid_text = ("<h3><li>{author} at {time}</h3>\n"
                            "<p>{text}</li>").format(
                                author=kid_data.get('by', 'Someone'),
                                time=self._format_time(kid_data.get('time')),
                                text=kid_data.get('text'))
                post_text += kid_text

            if post_kids:
                post_text += "</ol>\n"

            self.feed.append_item(title=post_title,
                                  author=post_author,
                                  link=post_url,
                                  date=post_time,
                                  description=post_text)
    def make_xml(self):
        "Generate xml in `self.xml` from `self.feed`"
        self.xml = self.feed.get_xml()
        return


    def _get_post_ids(self, url):
        "Return a list containing the post ids."
        return self._get_json_data(url)[:self.numposts]

    def _get_post_data(self, post_id):
        """
        Retrieve the content of the url corresponding to ``post_id`` and
        parse it as a dictionary.
        """
        data = self._get_json_data(HN_API_BASE_URL + "item/" \
                                  + str(post_id) + ".json?print=pretty")
        return data

    @staticmethod
    def _format_time(epochtime):
        "Translate Unix time into `Mon, 1 Jan 2015 12:01:01 -4:00` format."
        if not epochtime:
            epochtime = time.localtime()
        return time.strftime("%a, %d %B %Y %X %Z", time.gmtime(epochtime))

    @staticmethod
    def _get_json_data(url):
        "Retrieve the content of ``url`` and parse it as a dictionary."
        response = urlopen(url)
        data = response.read().decode(encoding='UTF-8')
        return json.loads(data)


def main_top():
    "Generate the feed for TOP posts"
    hntest = HNrss(HN_TOP_URL)
    hntest.generate_feed()
    return hntest

if __name__ == "__main__":
    HN_TOP = main_top()
    with open("testrss.html", "w") as f:
        f.write(HN_TOP.feed.get_xml())
