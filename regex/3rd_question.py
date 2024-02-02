"""
Print the same text as follows:

#1.
# Event: Workshop & Tutorial proposals due
# Date: November 21, 2019

#2.
# Event: Notification of acceptance
# Date: December 1, 2019

# etc.

"""

import re

text = """
Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020
"""


def return_event_and_date(text):
    pattern = re.compile(r"(.*?):(.*?)\n")
    matches = re.findall(pattern, text)

    for x, match in enumerate(matches, start=1):
        print(f"{x}.")
        print("Event:", match[0])
        print("Date:", match[1])
        print()


return_event_and_date(text)
