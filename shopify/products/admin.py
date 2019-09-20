from django.contrib import admin
from .models import Product,Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ['title','price','image','stock','updated']
    list_editable = ['price','stock']
    list_filter = ['price','stock']
    readonly_fields = ['updated']
    # prepopulated_fields = {"slug": ('title',)}
    class Meta:
        model= Product

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

    # class Meta:
    #     model= Category 


admin.site.register(Category, CategoryAdmin)

