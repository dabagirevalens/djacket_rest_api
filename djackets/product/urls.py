from django.urls import path, include

from product import views 

urlpatterns =[
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/', views.ProductSearch.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDeatails.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetails.as_view())
]