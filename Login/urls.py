from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('sfondo', views.bg, name="bg"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)