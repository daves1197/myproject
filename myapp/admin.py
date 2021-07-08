from django.contrib import admin

# Register your models here.
from .models import User, Seminar, Review, Category, Partis
# Register your models here.
admin.site.register(User)
admin.site.register(Seminar)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Partis)
