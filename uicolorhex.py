#!/usr/bin/env python3

import re
import sys

def convert(in_hex):
    in_hex = in_hex.strip().upper()
    m = re.search('#([A-F,0-9]{2})([A-F,0-9]{2})([A-F,0-9]{2})([A-F,0-9]{2})?', in_hex)

    try:
        int(m.group(1), 16)
        int(m.group(2), 16)
        int(m.group(3), 16)
        assert len(in_hex) == 7 or len(in_hex) != 8
    except (IndexError, ValueError, AttributeError, AssertionError):
        return "UIColor()"

    if m.group(4) != None:
        try:
            int(m.group(4),16)
            assert len(in_hex) <= 9
        except (IndexError, ValueError, AttributeError, AssertionError):
            return "UIColor()"
        return f"UIColor(red: {int(m.group(1),16)}/255, green: {int(m.group(2),16)}/255, blue: {int(m.group(3),16)}/255, alpha: {int(m.group(4),16)}/255)"
    else:
        return f"UIColor(red: {int(m.group(1),16)}/255, green: {int(m.group(2),16)}/255, blue: {int(m.group(3),16)}/255, alpha: 1.0)"


if __name__ == '__main__':
    print(convert(input()))