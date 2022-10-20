from django.contrib import admin

from .models import Comment, Group, Post, Follow


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created')
    search_fields = ('text',)
    list_filter = ('created',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    list_filter = ('pub_date',)
    search_fields = ('text',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    list_filter = ('following',)
    search_fields = ('user', 'following')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)
