from django.contrib import admin
from .models import Authentication, Categories, SellerProfile

# Register your models here.
admin.site.register(Authentication)
admin.site.register(SellerProfile)
admin.site.register(Categories)
