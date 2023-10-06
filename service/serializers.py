from django.utils.translation import gettext as _
from rest_framework import serializers

from .models import Employee, Store, Visit


class RequestMobilePhone(serializers.Serializer):
    mobile = serializers.CharField(
        max_length=255, required=True, write_only=True,
        error_messages={
           'required': _('Необходимо предоставить номер телефона..')
                       }
        )

    def validate_mobile(self, value):
        try:
            Employee.objects.get(mobile=value)
        except Employee.DoesNotExist:
            raise serializers.ValidationError(
                _('Пользователя с таким номером не существует')
            )
        else:
            return value


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name')
        read_only_fields = ('id', 'name')


class VisitInputSerializer(serializers.ModelSerializer):
    store_id = serializers.IntegerField(min_value=0, required=True)

    class Meta:
        model = Visit
        fields = ('store_id', 'latitude', 'longitude')


class VisitOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ('id', 'datetime_visited')
        extra_kwargs = {'datetime_visited': {'format': '%Y-%m-%d %H:%M:%S'}}
