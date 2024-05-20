from rest_framework import mixins, viewsets

class ListCreateMixin(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass