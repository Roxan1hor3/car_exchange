from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Car)
admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(Question)
admin.site.register(Message)
admin.site.register(Wish)
admin.site.register(Answer)
