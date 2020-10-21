from django.contrib import admin
 
from .models import Post,Box,Box1,Post1,Document
 
admin.site.register(Post)
admin.site.register(Box)
admin.site.register(Box1)
admin.site.register(Post1)
admin.site.register(Document)
 
from .models import PostImage
 
class PostImageAdmin(admin.StackedInline):
    model = PostImage
'''
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Post
''' 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass




