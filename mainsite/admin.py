from django.contrib import admin
from .models import Post,Message

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_display=('title','slug','pub_date')
 
class MessageAdmin(admin.ModelAdmin):
  list_display=('name','words','address','date')

admin.site.register(Post,PostAdmin)
admin.site.register(Message,MessageAdmin)