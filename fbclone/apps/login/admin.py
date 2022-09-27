from django.contrib import admin
from .models import Post,Like,Comment,Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	# list_display = ('title','image','author')
	list_display = ('title','author','likeuser','likeusers')
admin.site.register(Post,PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Comments)



