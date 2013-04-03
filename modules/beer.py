#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import os
import random

rand_str = ["X-Bot asks %s to see some ID - NO (beer) for you!!",
" a little early for (beer) %s, You should wait for happy hour",
"X-Bot pours %s a cold foamy glass of (beer) Cheers mate!",
"X-Bot says %s had a rough day how about a shot of Jager instead?",
"%s I do not normally drink (beer) but when I do I choose XX" ]

#from rand_str import choice
#print random.choice(rand_str) % os.environ["SKYPE_FULLNAME"]

print random.choice(rand_str) % os.environ["SKYPE_FULLNAME"]

# print "X-Bot asks %s to see some ID - NO (beer) for you!!" % os.environ["SKYPE_FULLNAME"]
