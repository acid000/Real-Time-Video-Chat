"""
ASGI config for videochat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videochat.settings')
from channels.security.websocket import AllowedHostsOriginValidator
from video.consumers import VideoChat
from django.urls import path
application = ProtocolTypeRouter(
    {
        
        "websocket": AllowedHostsOriginValidator(
           URLRouter(
                 [
                    path('ws/',VideoChat.as_asgi())
                 ]
           )
        ),
    }
)
