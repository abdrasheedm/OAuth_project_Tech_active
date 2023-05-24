from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 3  # Set the number of items per page
    page_query_param = 'page'  # Set the query parameter for page number
    page_size_query_param = 'page_size'  # Set the query parameter for page size
    max_page_size = 100  # Set the maximum allowed page size

    def get_paginated_response(self, data):
        next_page = self.get_next_link()
        previous_page = self.get_previous_link()
        return Response({
            'next': next_page,
            'previous': previous_page,
            'count': self.page.paginator.count,
            'results': data
        })