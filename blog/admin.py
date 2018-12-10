from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulate_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

#khs123/12345