#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
