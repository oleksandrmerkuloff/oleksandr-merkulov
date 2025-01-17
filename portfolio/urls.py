from django.urls import path

from . import views


urlpatterns = [
    path('', views.portfolio_page, name='portfolio'),
    path('<slug:project_slug>', views.single_project, name='single-project-page'),
    path('<int:project_pk>/like', views.like_project, name='like_project'),
]
