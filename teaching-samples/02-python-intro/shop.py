"""
A module of our own: functions of a small shop.

This file is not a program that is started. Other programs import it (see 09_modules.py).
"""

VAT_RATE = 20   # in percent


def price_with_vat(net_price):
    """Returns the price with the value added tax."""
    return net_price * (1 + VAT_RATE / 100)
