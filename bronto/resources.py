# -*- coding: utf-8 -*-

from pyramid.interfaces import IRootFactory
from zope.interface import implementer
from .interfaces import IFallback


@implementer(IFallback, IRootFactory)
class Fallback:

    def __init__(self, request):
        """
        :type request: pyramid.request.Request
        """
        self.request = request
