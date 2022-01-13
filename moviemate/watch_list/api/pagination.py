from rest_framework.pagination import PageNumberPagination


class WatchListPagination(PageNumberPagination):
    page_size=10
    # page_query_param= 'records'
    page_size_query_param = 'size'
    max_page_size = 5
    # last_page_strings = 'last'