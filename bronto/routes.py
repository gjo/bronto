# -*- coding: utf-8 -*-


def includeme(config):
    """
    :type config: pyramid.config.Configurator
    """

    config.add_jsonrpc_endpoint('jsonrpc', pattern='/api/rpc',
                                request_method='POST',
                                header='Content-Type:application/json.*')

    # Core API
    config.add_route('root', pattern='/')
    config.add_route('rest_api.cache.invalidate',
                     pattern='/api/rest/cache/invalidate')
