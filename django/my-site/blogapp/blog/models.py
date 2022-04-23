from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=True,db_index=True,unique=True,editable=False,blank=True)


    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(max_length=50,upload_to='blogs')
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    description = RichTextField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE,db_column='categoryId')
    categories = models.ManyToManyField(Category)


    class Meta:
        db_table = 'blog'

    def __str__(self):
        return self.title

    # Save fonksiyonunu override ettik.
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)




