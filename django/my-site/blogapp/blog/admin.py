from django.contrib import admin
from .models import Blog,Category
from django.utils.safestring import mark_safe

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','isActive','isHome','slug','selected_categories')
    list_editable = ('isActive','isHome')
    search_fields = ('title',)
    readonly_fields = ('slug',)
    list_filter = ('isActive','isHome','categories')

    def selected_categories(self,obj):
        html = '<ul>'

        # obj burada blog u temsil eder.
        for category in obj.categories.all():
            html += '<li>' + category.name + '</li>'

        html += '</ul>'

        return mark_safe(html)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)