from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Car)
admin.site.register(BodyType)
admin.site.register(Mark)
admin.site.register(Mileage)
admin.site.register(Transmission)
admin.site.register(Year)
admin.site.register(Drivetrain)
admin.site.register(Color)
admin.site.register(Question)
admin.site.register(Message)
admin.site.register(WishList)
admin.site.register(Answer)
