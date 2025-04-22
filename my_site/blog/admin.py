from django.contrib import admin
from .models import Post, Author, Tag

# Register your moadels here.
admin.site.register(Post)
admin.site.register(Author)     
admin.site.register(Tag)

