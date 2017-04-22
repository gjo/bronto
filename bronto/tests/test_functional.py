# -*- coding: utf-8 -*-

import json
import unittest
import webob


class FunctionalTestCase(unittest.TestCase):

    def _make_wsgi_app(self, settings):
        """
        :type settings: dict
        :return: WSGI App
        """
        from .. import app_factory
        app = app_factory({}, **settings)
        return app

    def _make_jsonrpc_req(self, method, params):
        """
        :type method: str
        :type params: dict
        :rtype: webob.Request
        """
        req = webob.Request.blank(path='/api/rpc', headers={
            'Content-Type': 'application/json',
        }, POST=json.dumps({
            # FIXME: pyramid_rpc isnot support JSON-RPC 1.0
            'id': '__testing_dummy__',
            'jsonrpc': '2.0',

            'method': method,
            'params': params,
        }))
        return req

    def test_core_api_discovery(self):
        app = self._make_wsgi_app({})
        req = webob.Request.blank(path='/', headers={
            'Accept': 'application/xrds+xml',
        })
        resp = req.get_response(app)
        self.assertEqual(resp.status_code, 200)

    def test_core_api_cache_invalidate_rest(self):
        app = self._make_wsgi_app({})
        req = webob.Request.blank(path='/api/rest/cache/invalidate', headers={
            'Content-Type': 'application/json',
        }, POST=json.dumps({'invalidationKeys':[]}))
        resp = req.get_response(app)
        self.assertEqual(resp.status_code, 200)

    def test_core_api_cache_invalidate_rpc(self):
        app = self._make_wsgi_app({})
        req = self._make_jsonrpc_req('cache.invalidate', {
            'invalidationKeys': [],
        })
        resp = req.get_response(app)
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json_body['result'], list)

    def test_core_api_system_list_methods(self):
        app = self._make_wsgi_app({})
        req = self._make_jsonrpc_req('system.listMethods', {})
        resp = req.get_response(app)
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json_body['result'], list)
        # FIXME: pyramid_rpc isnot supported

    def test_core_api_system_method_help(self):
        app = self._make_wsgi_app({})
        req = self._make_jsonrpc_req('system.methodHelp', {
            'methodName': 'system.methodHelp'
        })
        resp = req.get_response(app)
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json_body['result'], str)
        # FIXME: pyramid_rpc isnot supported

    def test_core_api_system_method_signatures(self):
        app = self._make_wsgi_app({})
        req = self._make_jsonrpc_req('system.methodSignatures', {
            'methodName': 'system.methodSignatures'
        })
        resp = req.get_response(app)
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json_body['result'], dict)
        # FIXME: pyramid_rpc isnot supported
