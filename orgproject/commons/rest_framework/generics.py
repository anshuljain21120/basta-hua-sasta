from rest_framework import viewsets, mixins

from orgproject.commons.mixins.model_mixins import SafeDeleteModelMixin


class CURLViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    Create-Update-Retrieve-List Model ViewSet
    """
    http_method_names = ["get", "post", "put", "patch", "head", "options", "trace"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class SafeDeleteCompleteViewSet(CURLViewSet, SafeDeleteModelMixin):
    http_method_names = CURLViewSet.http_method_names + ["delete"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
