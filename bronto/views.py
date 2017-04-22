# -*- coding: utf-8 -*-

from pyramid.view import view_config
from pyramid_rpc.jsonrpc import jsonrpc_method
from .schemas import (
    cache_invalidate_schema,
)


@view_config(route_name='rest_api.cache.invalidate', request_method='POST',
             header='Content-Type:application/json.*', renderer='json')
def cache_invalidate(request):
    """
    defined in Core API Specification 8.1.1

    :type request: pyramid.request.Request
    :rtype: dict
    """
    verified = cache_invalidate_schema.bind().deserialize(request.json_body)
    return verified


@jsonrpc_method(method='cache.invalidate', endpoint='jsonrpc')
def cache_invalidate_rpc(request, invalidationKeys):
    """
    defined in Core API Specification 8.1.1

    :type request: pyramid.request.Request
    :type invalidationKeys: list[str]
    :rtype: list[str]
    """
    verified = cache_invalidate_schema.bind().deserialize({
        'invalidationKeys': invalidationKeys,
    })
    return verified['invalidationKeys']


@view_config(route_name='root', request_method='GET',
             accept='application/xrds+xml')
def discovery(request):
    """
    defined in Core API Specification 7

    :type request: pyramid.request.Request
    :rtype: dict
    """
    resp = request.response
    resp.content = """\
<XRDS xmlns="xri://$xrds">
   <XRD xmlns:simple="http://xrds-simple.net/core/1.0" xmlns="xri://$XRD*($v*2.0)" version="2.0">
       <Type>xri://$xrds*simple</Type>
       <Service>
         <Type>http://ns.opensocial.org/2008/opensocial/people</Type>
         <URI>http://api.example.org/people</URI>
       </Service>
       <Service>
         <Type>http://ns.opensocial.org/2008/opensocial/groups</Type>
         <URI>http://api.example.org/groups</URI>
       </Service>
       <Service>
         <Type>http://ns.opensocial.org/2008/opensocial/activities</Type>
         <URI>http://api.example.org/activities</URI>
       </Service>
       <Service>
         <Type>http://ns.opensocial.org//2008/opensocial/appData</Type>
         <URI>http://api.example.org/appData</URI>
       </Service>
       <Service>
         <Type>http://ns.opensocial.org/2008/opensocial/cache/invalidate</Type>
         <URI>http://api.example.org/cache/invalidate</URI>
       </Service>
       <Service>
         <Type>http://ns.opensocial.org/2008/opensocial/messages</Type>
         <URI>http://api.example.org/messages</URI>
       </Service>
       <Service>
          <Type>http://ns.opensocial.org/2008/opensocial/albums</Type>
          <URI>http://api.example.org/albums</URI>
       </Service>
       <Service>
          <Type>http://ns.opensocial.org/2008/opensocial/mediaItems</Type>
          <URI>http://api.example.org/mediaItems</URI>
       </Service>
   </XRD>
</XRDS>
"""
    return resp
