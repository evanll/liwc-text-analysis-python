# -*- coding: utf-8 -*-
"""
Written by Evan Lalopoulos <evan.lalopoulos.2017@my.bristol.ac.uk>
University of Bristol, May 2018
Copyright (C) - All Rights Reserved
"""

from .liwc import Liwc

WORD_CAT_DICT_1 = {
    "love": [
        "affect",
        "posemo"
    ],
    "loved": [
        "affect",
        "posemo"
    ]
}

WORD_CAT_DICT_2 = {
    "abandon*": [
        "affect",
        "negemo"
    ],
    "absolute": [
        "cogmech"
    ],
    "love": [
        "affect",
        "posemo"
    ]
}


def test_build_trie():
    expected = {
        "l": {
            "o": {
                "v": {
                    "e": {
                        "$": [
                            "affect",
                            "posemo"
                        ],
                        "d": {
                            "$": [
                                "affect",
                                "posemo"
                            ]
                        }
                    }
                }
            }
        }
    }
    assert Liwc._build_char_trie(WORD_CAT_DICT_1) == expected


def test_build_trie_wildcard():
    expected = {
        "a": {
            "b": {
                "a": {
                    "n": {
                        "d": {
                            "o": {
                                "n": {
                                    "*": [
                                        "affect",
                                        "negemo"
                                    ],
                                    "$": [
                                        "affect",
                                        "negemo"
                                    ]
                                }
                            }
                        }
                    }
                },
                "s": {
                    "o": {
                        "l": {
                            "u": {
                                "t": {
                                    "e": {
                                        "$": [
                                            "cogmech"
                                        ]
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "l": {
            "o": {
                "v": {
                    "e": {
                        "$": [
                            "affect",
                            "posemo"
                        ]
                    }
                }
            }
        }
    }

    assert Liwc._build_char_trie(WORD_CAT_DICT_2) == expected


def test_search_trie():
    trie = Liwc._build_char_trie(WORD_CAT_DICT_1)

    assert Liwc._search_trie(trie, 'love') == ["affect", "posemo"]
    assert Liwc._search_trie(trie, 'loved') == ["affect", "posemo"]


def test_search_wildcard():
    trie = Liwc._build_char_trie(WORD_CAT_DICT_2)

    assert Liwc._search_trie(trie, 'abandon') == ["affect", "negemo"]
    assert Liwc._search_trie(trie, 'abandonment') == ["affect", "negemo"]
