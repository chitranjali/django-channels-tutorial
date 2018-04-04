from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)),
})

try:
    import ptvsd
except:
    pass
else:
    import logging
    logger = logging.getLogger('daphne.server')
    port = 8001
    secret = "channels"
    ptvsd.enable_attach(secret=secret, address=('0.0.0.0', port))
    logger.info('Debugger attached (port={}, secret={})'.format(port, secret))
