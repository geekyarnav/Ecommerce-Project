"""shopify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# """
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from products.views import ProductListView 
from django.views.generic import TemplateView
# from products.views import product_list_view 
# from products.views import product_detail_view
# from products.views import product_create_view
# from products.views import ListView

# from products.views import ProductDetailView
# from products.views import CreateView
from .views import home_page,about_page,contact_page,login_page,registration_page

urlpatterns = [
    # path('index/',index),
    #path('', home),
    path('admin/', admin.site.urls),
    path('',home_page,name="home"),
    path('contact/',contact_page,name="contact"),
    path('about/',about_page,name="about"),
    path('login/',login_page,name="login"),
    path('register/',registration_page,name="register"),
    path('bootstrap/',TemplateView.as_view(template_name="bootstrap/example.html")),
    path('products/',ProductListView.as_view(),name="products"),
    
    # path('products-fbv/',product_list_view),
    # url(r'^(?P<pk>\d+)/$', include(ProductListView),ProductDetailView.as_view(), name="product-detail"),
    # path('products-detail/',ProductDetailView.as_view()),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)