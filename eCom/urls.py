from django.urls import path
from. import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('product/', views.ProductList.as_view()),
    # path('update/<int:pk>', views.ProductDetail.as_view()),
    # path('user/profile', views.UserProfile.as_view()),
    path('product/<int:pk>', views.ProductDetail.as_view()),
    # path('cart/', views.CartList.as_view()),
    # path('cart/<int:pk>', views.CartDetail.as_view()),
    # path('product/<int:pk>/delete',views.ProductDetail.as_view()),
]    