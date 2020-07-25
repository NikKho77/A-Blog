from django.contrib import admin
from .models import Post, History,Contacts,Prices,Hours
# Register your models here.
admin.site.register(Post)
admin.site.register(History)
admin.site.register(Contacts)
admin.site.register(Prices)
admin.site.register(Hours)