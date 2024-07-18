from django.db import models

from django.db import migrations, models

class Category_subcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)

    class Meta:
        db_table = 'v_category_subcategory'

    def __str__(self):
        return f"Category_subcategory #{self.id} - {self.category}: {self.sub_category}"


class Book(models.Model):
    title = models.CharField(max_length=100, default='Unknown')
    author = models.CharField(max_length=50, default='Unknown')
    published_date = models.DateField()
    category_subcategory = models.ForeignKey(Category_subcategory, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    category = models.ForeignKey(Category_subcategory, on_delete=models.CASCADE, related_name='subcategories', db_column='cat_id')
    subcategory_name = models.CharField(max_length=255, null=True, blank=True)
    is_scrap = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    last_scrap_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v_subcategory'
    
    def __str__(self):
        return self.subcategory_name





