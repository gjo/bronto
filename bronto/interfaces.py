# -*- coding: utf-8 -*-

from zope.interface import Interface


class IFallback(Interface):
    """
    marker for default request context.
    """
