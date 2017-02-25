#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Produces an automated summary of the webpage.

Using the LSA Summarizer from sumy, this attempts to create an automated
summarizer of the content at a given url. There are very many unhandled
edge-cases, so use with some caution.

WARNING
-------
  For some pages, this summarizer can hang. So this should be run with
  some other memory management tools.



COPYRIGHT NOTICE
---------------
Copyright 2016-2017 David Lowry-Duda

You are free to redistribute and/or modify HNRSS under the
terms of the MIT License. A copy of this license should be made available with
the source.

I'm happy if you find HNRSS useful, but be advised that
it comes WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""


from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"

stemmer = Stemmer(LANGUAGE)
summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

def summarize(url, sent_count=10):
    "Produces `sent_cout` sentence summaries of `url`."
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    return " ".join([str(sentence) for sentence
                     in summarizer(parser.document, sent_count)])
