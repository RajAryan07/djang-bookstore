from My_Books.models import Form
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Form
        fields = '__all__'
