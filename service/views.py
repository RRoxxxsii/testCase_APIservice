from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from service.models import Store, Visit
from service.serializers import (RequestMobilePhone, StoreSerializer,
                                 VisitInputSerializer, VisitOutputSerializer)


class ListStoreAPIView(GenericAPIView):
    """
    Запрашивает номер телефона, возвращает список торговых точек привязанных
    к введенному номеру, где ТТ: id, name
    """
    mobile_serializer_class = RequestMobilePhone
    serializer_class = StoreSerializer

    def post(self, request):
        mobile_serializer = self.mobile_serializer_class(data=request.data)
        if mobile_serializer.is_valid():
            mobile = mobile_serializer.validated_data['mobile']
            stores = Store.objects.filter(user__mobile=mobile)
            serializer = self.serializer_class(stores, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VisitStoreAPIView(CreateAPIView):
    """
    Создает посещение ТТ. Запрашивает номер телефона(mobile), ID ТТ(store_id),
    ширину(latitude) и долготу(longitude). Возвращает ID посещения(id) и время
    посещения(datetime_visited).
    """
    serializer_class = VisitInputSerializer
    serializer_output_class = VisitOutputSerializer
    mobile_serializer_class = RequestMobilePhone

    def create(self, request, *args, **kwargs):

        mobile = request.data.get('mobile')
        mobile_serializer = self.mobile_serializer_class(
            data={'mobile': mobile}
        )
        if mobile_serializer.is_valid():
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            store_id = serializer.data.get('store_id')
            longitude = serializer.data.get('longitude')
            latitude = serializer.data.get('latitude')

            # проверять, что переданный номер телефона Работника привязан к ТТ
            if not Store.objects.filter(id=store_id, user__mobile=mobile).exists():
                return Response(
                    {'error': _('Мобильный номер не привязан к переданной точке.')},
                    status=status.HTTP_400_BAD_REQUEST)

            visit = Visit.objects.create(
                store_id=store_id,
                longitude=longitude,
                latitude=latitude
            )

            serializer = self.serializer_output_class(instance=visit)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
