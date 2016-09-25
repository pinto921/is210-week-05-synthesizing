#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""code to to run today's date"""

import datetime

CURDATE = None

def get_current_date():
    """current date"""
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get-current_date()
    print CURDATE
