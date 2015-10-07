from rest_framework.routers import Route, SimpleRouter


class DeviceRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}/{lookup}/devices',
            mapping={'get': 'list',
                     'post': 'perform_create'},
            name='{basename}-devices-list',
            initkwargs={'suffix': 'devices-list'}
        )
    ]