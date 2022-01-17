#!/usr/bin/python3
from logging import exception


def raise_exception():
    try:
        raise_exception()
    except exception as ex:
        pass
