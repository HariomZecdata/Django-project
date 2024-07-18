# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('harry', views.my_view_function, name='my_view'),  # URL pattern for a view function
    path('get_category', views.my_view_function, name='my_view'),
    path('api/add_category', views.category_post_api, name='category_post_api'),  # Ensure this ends with a slash
    path('api/add_book', views.book_post_api, name='book_post_api'),  # Ensure this ends with a slash
    path('api/count_category', views.category_group_by_view, name='book_post_api'),  # Ensure this ends with a slash
    path('api/subcategory', views.subcategory_function, name='get_subcategory_api')
]


