"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token  
from crudapp import views as myapp_views
from django.urls import include, path
from rest_framework import routers
from core import views
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'friends', myapp_views.FriendViewset)
router.register(r'belongings', myapp_views.BelongingViewset)
router.register(r'borrowings', myapp_views.BorrowedViewset)

urlpatterns = [
    
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
    path('api/crudops/', include(router.urls)),
]
