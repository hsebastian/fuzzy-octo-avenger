#!/usr/bin/env python
"""
urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough.

linkedlist.php?nothing=12345

http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
"""
import re

import requests


nothing = 12345
for i in range(400):
    if i == 85:
        nothing = str(int(nothing) / 2)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing
    print i, url
    response = requests.get(url)
    print response.text
    match = re.search('and the next nothing is (\d+)', response.text)
    assert match is not None, "Answer found: %s" % response.text
    nothing = match.group(1)

