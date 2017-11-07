from django.contrib import admin
from bookApp.models import *

admin.site.register(Book)
admin.site.register(Writer)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(User)
# Register your models here.
