#!/usr/bin/env python3
"""Minimal operations"""


def minOperations(n):
    """Operations"""
    if n == 1:
        return 0

    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i

    return operations if n == 1 else 0
