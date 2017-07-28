#!/usr/bin/env python3
"""This is module docstring."""

import logging

_logger = logging.getLogger(__name__)


def hello_world(user=None):
    """Hello world function.

    This is longer description for hello_world function that can keep additional information. It is not necessary to
    include this for each function. And here is a usage example:

    >>> from f8a import hello_world
    >>> hello_world('f8a_user')

    :param user: a user to which hello should be said
    :type user: str
    :return: always 0
    :rtype: int
    """
    _logger.debug("Inside hello_world function")
    print("Hello, {}!".format(user or 'fabric8-analytics'))

    return 0
