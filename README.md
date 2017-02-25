
HNRSS
=========

This is an RSS 2.0 generator for HackerNews, which remarkably does not have an RSS feed. In addition to correcting this very basic deficiency, this includes the top five comments in the data for the RSS feed for easier detection of interesting content from afar.

HNRSS also attempts to create an automated summary of linked webpages.

This relies on [feedmaker](https://github.com/davidlowryduda/feedmaker) for the generation of the feed itself.

### Fruits of this labor

I currently use this to regularly generate RSS feeds for HackerNews. These are available at

1. http://davidlowryduda.com/static/HN_rss/toprss.html [For the Front Page]
2. http://davidlowryduda.com/static/HN_rss/bestrss.html [For the Best List]
3. (I am not currently generating newly added links, but I have in the past)

These are updated every few hours and are cached. As top comments can change,
new feeds are generated each time, overwriting previous feeds. It may be a good
idea to do this in a smarter way in the future, but I'm currently pretty happy
with the feeds.

If you have any questions or comments, feel free to reach out to me.


### Caution

Note that HNRSS can sometimes hang. This is usually caused by an error during
automated summarization. Therefore it is usually a good idea to have good
process management that monitors the time and memory usage of this program. I
am currently using [timeout](https://github.com/pshved/timeout) with some
success.
