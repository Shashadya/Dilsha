from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.storehome, name='storehome'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('reviews/', views.reviews, name='reviews'),
    path('category/', views.category, name='category'),
    # path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>', views.product, name='product'),
    path('shop/<str:category>/', views.shop, name='shop_by_category'),

]
urlpatterns += staticfiles_urlpatterns()
