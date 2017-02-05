#!/usr/bin python
# -*- coding: utf-8 -*-
import ngram
sentences=["su","süt"]
search_try= ngram.NGram(sentences)
print search_try.search("sut")
