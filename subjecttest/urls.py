from django.urls import path
from .views import (QuesTestApiView, QuesTestDetailApiView, QuesTestUpdateApiView,
                    QuesTestDeleteApiView, QuesTestCreateApiView)

urlpatterns = [
    path('',QuesTestApiView.as_view(),),
    path('create/',QuesTestCreateApiView.as_view(),),
    path('<int:pk>/',QuesTestDetailApiView.as_view(),),
    path('<int:pk>/update/',QuesTestUpdateApiView.as_view(),),
    path('<int:pk>/delete/',QuesTestDeleteApiView.as_view(),),



]
