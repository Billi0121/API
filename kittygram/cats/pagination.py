from rest_framework.pagination import PageNumberPagination
from .models import *
from rest_framework import pagination
from rest_framework.response import Response

class CatsPagination(pagination.BasePagination):
    # page = 5
    def paginate_queryset(self, queryset, request, view=None):
        queryset = Cat.objects.all()
        return queryset
    
    def get_paginated_response(self, data):
        return Response({
            # 'count': self.page.paginator.count,
            'results': data
        })
