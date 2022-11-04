from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):
 #  ordering = 'instructor_id'
  # cursor_query_param = 'cu'
  max_page_size = 10
  page_query_param = 'p'
  page_size_query_param = 'count'
"""
class CustomPageNumberPagination(pagination.LimitOffsetPagination):
 limit_query_param = 'limit'
 offset_query_param = 'offset'

class CustomPageNumberPagination(pagination.CursorPagination):
 cursor_query_param = 'cursor'

"""