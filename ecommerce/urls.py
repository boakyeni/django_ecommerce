"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from elasticsearch_dsl import Search
from rest_framework import routers

from ecommerce.drf import views
from ecommerce.search.views import SearchProductInventory

router = routers.DefaultRouter()
router.register(r"api", views.AllProductViewset, basename="allproducts")
router.register(
    r"product/(?P<slug>[^/.]+)",
    views.ProductInventoryViewset,
    basename="products",
)
router.register(
    r"category/(?P<slug>[^/.]+)",
    views.ProductByCategory,
    basename="productbycategory",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("ecommerce.demo.urls", namespace="demo")),
    path("", include(router.urls)),
    path("search/<str:query>/", SearchProductInventory.as_view()),
]
