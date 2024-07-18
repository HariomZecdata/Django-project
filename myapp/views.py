from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category_subcategory , Subcategory
from .serializers import BookSerializer, CategorySerializer , SubcategorySerialize
import json
from django.db.models import Count
from django.core.cache import cache
from django.http import JsonResponse

def my_view_function(request):
    # if request.method == 'GET':
    #     # Define cache key
    #     cache_key = 'all_categories'
    #     # Try to get data from cache
    #     cached_data = cache.get(cache_key)
    #     # print("cached_data",cached_data)
    #     if cached_data:
    #         # Use cached data if available
    #         serializer_data = cached_data
    #         print("Using cached data")
    #     else:
    #         # Fetch all records from the database
    #         cat = Category_subcategory.objects.all()
    #         serializer = CategorySerializer(cat, many=True)
    #         serializer_data = serializer.data
    #         # Cache the serialized data for 15 minutes
    #         cache.set(cache_key, serializer_data, timeout=900)  # 15 minutes
    #         print("Using database data")
            # 'categories': serializer_data
        return render(request, 'my_template.html')
    # else:
    #     # Handle invalid HTTP method
    #     return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
# def category_group_by_view(request):
#     category_counts = Category_subcategory.objects.values('sub_category').annotate(num_occurrences=Count('category')).filter(num_occurrences__gt=2)
#     context = {
#         'category_counts': category_counts
#     }
#     return render(request, 'category_group_by.html', context)

# @csrf_exempt
# def category_post_api(request):
#     print("-------------------")
#     print(request.method)
#     if request.method == 'POST':
#         print("-------------------")
#         try:
#             data = json.loads(request.body)
#             print(data)
#             category = data.get('category')
#             sub_category = data.get('sub_category')
            
#             # Create and save new Category_subcategory object
#             new_category = Category_subcategory(category=category, sub_category=sub_category)
#             new_category.save()

#             response_data = {
#                 "message": "successfully data inserted",
#                 'id': new_category.id,
#                 'category': new_category.category,
#                 'sub_category': new_category.sub_category,
#             }
#             return JsonResponse(response_data, status=201)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#         except KeyError:
#             return JsonResponse({'error': 'Missing category or sub_category'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

# @csrf_exempt
# def book_post_api(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         serializer = BookSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

# def subcategory_function(request):
#     if request.method == 'GET':
#         print("---------------------")
#         # Fetch all records from the view
#         cat = Subcategory.objects.select_related('category').values('subcategory_name').annotate(num_occurrences=Count('id'))
#         print("----------------------")
#         serializer = SubcategorySerialize(cat, many = True)
#         print("serializer",serializer.data)
#         return render(request, 'subcategory_template.html', {
#             'sub_categories': serializer.data
#         })
  
#     else:
#         # Handle invalid HTTP method
#         return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
