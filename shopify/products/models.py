from django.db import models
import random
import os
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True ) 
    slug = models.SlugField(max_length=200, db_index=True,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category' , args=[self.slug])  

def get_filname_ext(filename):
    base_name=os.path.basename(filter)
    name,ext = os.path.splittext(filter)
    return name,ext

def upload_image_path(instance,filename):
    # print(instance)
    # print(filename)
    new_filename = random.randomint(1,965678743)
    name, ext = get_filename_ext(filename)
    final_filename= f'{new_filename}{ext}'
    return f'products/{new_filename}{final_filename}'

class Product(models.Model):
    title       =models.CharField(max_length=200,)
    description =models.TextField(blank=True,null=True)
    price       =models.DecimalField(decimal_places=2,max_digits=100)
    updated     = models.DateTimeField(auto_now=True)
    image       = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    stock       = models.PositiveIntegerField(default=10)
    #timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    #active = models.BooleanField(default=True)
    # slug = models.SlugField()
    # category = models.ForeignKey(Category,default=1,verbose_name="category",on_delete='cascade')
    # name = models.CharField(max_length=200, db_index=True )
    # saleprice = models.DecimalField(decimal_places=2,max_digits=100)
    # available = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    

    # class Meta:
    #     ordering = ('-created',)
    #     index_together = (('id','slug'),)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('products:product_detail' , args=[self.id, self.slug])  

