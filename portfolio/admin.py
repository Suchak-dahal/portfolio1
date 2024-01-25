from django.contrib import admin
from .models import *

# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'authname',
                    'img',
                    'timeStamp')
    search_fields=('title','authname')
    list_filter=['timeStamp']

admin.site.register(Blogs, BlogsAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'phonenumber',
                    'description')
    search_fields=('name','email')
    list_filter=['phonenumber']

admin.site.register(Contact, ContactAdmin)

