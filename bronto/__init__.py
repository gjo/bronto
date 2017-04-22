# -*- coding: utf-8 -*-

__version__ = '0.1.dev0'
default_settings = {
    # 'sqlalchemy.url': '',
}


def app_factory(global_config, **local_config):
    """
    :type global_config: dict[str, str]
    :type local_config: dict[str, str]
    :return: WSGI Application
    """
    from pyramid.config import Configurator
    from .resources import Fallback

    settings = default_settings.copy()
    settings.update(global_config)
    settings.update(local_config)

    config = Configurator(settings=settings, root_factory=Fallback)
    config.include('pyramid_rpc.jsonrpc')
    config.include('.routes')

    config.scan('.views')
    return config.make_wsgi_app()


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    app = app_factory({})
    server = make_server('', 6543, app)
    server.serve_forever()
