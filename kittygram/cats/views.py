from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import OwnerOrReadOnly, ReadOnly
from .throttling import CustomThrottle
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import *
# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    throttle_classes = (CustomThrottle,)
    throttle_scope = 'low_request'
    pagination_class = CatsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('name', 'color')
    search_fields = ('name', 'color')


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'retrive':
            return (ReadOnly())
        else:
            return super().get_permissions()