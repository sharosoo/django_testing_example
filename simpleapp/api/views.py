from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..models import Simple
from .serializers import SimpleSerializer


class SimpleListCreateView(ListCreateAPIView):
    queryset = Simple.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SimpleSerializer
    lookup_field = 'slug'


class SimpleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Simple.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = SimpleSerializer
    lookup_field = 'slug'
