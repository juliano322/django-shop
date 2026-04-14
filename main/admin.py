from django.contrib import admin

# Register your models here.

from .models import Category, Product


# list_display - параметры из моделс которые будут отображаться в админке которую мы будем видеть 
# prepopulated_fields - поля которые будут заполнены автомотически введя имя будет автоматически имя на английском
# list_filter - фильтровать именно для нас 
# list_editable позволяет редактировать 

@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','available','created','updated']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}



