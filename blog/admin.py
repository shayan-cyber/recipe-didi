from django.contrib import admin

# Register your models here.
from blog.models import Post
from blog.models import Contact
admin.site.register(Contact)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
