from django.contrib import admin
from .models import Post,Category,Comment, UserProfile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(UserProfile)
# Register your models here.
