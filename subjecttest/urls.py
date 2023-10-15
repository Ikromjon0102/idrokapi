from django.urls import path
from .views import (QuesTestApiView, QuesTestDetailApiView, QuesTestUpdateApiView,
                    QuesTestDeleteApiView, QuesTestCreateApiView, PupilsListView,
                    ParentsListView, TeachersListView, ThemeListView)

urlpatterns = [
    path('',QuesTestApiView.as_view(),),
    path('teachers/',TeachersListView.as_view(),),
    path('theme/',ThemeListView.as_view(),),
    path('pupils/',PupilsListView.as_view(),),
    path('parents/',ParentsListView.as_view(),),
    path('testcreate/',QuesTestCreateApiView.as_view(),),
    path('<int:pk>/',QuesTestDetailApiView.as_view(),),
    path('<int:pk>/update/',QuesTestUpdateApiView.as_view(),),
    path('<int:pk>/delete/',QuesTestDeleteApiView.as_view(),),
    path('',QuesTestDeleteApiView.as_view(),),



]
