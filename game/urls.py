from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views
from api.views import RegisterView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.game_list),
    url(r'^api/games/$', views.game_list),
    url(r'^api/games/(?P<pk>[0-9]+)$', views.getGame),
    path('register/', RegisterView.as_view(), name='auth_register'),
]