"""
write a function that would change the entered date (format dd.mm.yyyy) to yyyy mm dd. Don't worry about date logic,
we work purely with text.
"""

import re

date = "23.02.1994"


def reformat_date(date):
    pattern = re.compile(r"(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})")
    result = pattern.search(date)

    print(f"{result.group(3)}.{result.group(2)}.{result.group(1)}")


reformat_date(date)
