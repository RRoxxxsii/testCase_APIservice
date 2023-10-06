from django.urls import path

from service import views

urlpatterns = [
    path('stores/', views.ListStoreAPIView.as_view(), name='store-list'),
    path('visit/', views.VisitStoreAPIView.as_view(), name='create-visit')
]
