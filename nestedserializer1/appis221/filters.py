import django_filters

from .models import *
from .serializers import *

# class ProductFilter(django_filters.FilterSet):
#     rating1=django_filters.NumberFilter(field_name='rating',lookup_expr='iexact')
#     rating1_lt=django_filters.NumberFilter(field_name='rating',lookup_expr='lt')
#     rating1_gt = django_filters.NumberFilter(field_name='rating', lookup_expr='gt')
#     title1=django_filters.CharFilter(field_name='title',lookup_expr='lt')
#     class Meta:
#         model=Course
#         fields=['rating','instructor','title']

class StuformoduleFilter(django_filters.FilterSet):
    name_filter=django_filters.CharFilter(field_name='name',lookup_expr='lte')
    age_filter=django_filters.NumberFilter(field_name='age',lookup_expr='iexact')
    date_filter=django_filters.DateTimeFilter(field_name='created_at',lookup_expr='exact')
    module_name=django_filters.CharFilter(field_name='modules__module_name',lookup_expr='iexact')
    module_id = django_filters.NumberFilter(field_name='modules__id', lookup_expr='exact')
    module_id_gte=django_filters.NumberFilter(field_name='modules__id', lookup_expr='gt')
    module_id_lte=django_filters.NumberFilter(field_name='modules__id', lookup_expr='lte')
    class Meta:
        model=StudentforModule
        fields=['name','age','created_at','modules__id','modules__module_name']