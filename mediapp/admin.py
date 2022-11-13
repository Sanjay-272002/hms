from django.contrib import admin
from .models import domain,Doctor,Patient,Bed,Staff,Bed_num,oxygen,blood,organ,stafff,Item,OrderItem,Order
# Register your models here.
admin.site.register(domain)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Bed)
admin.site.register(Staff)
admin.site.register(Bed_num)
admin.site.register(oxygen)
admin.site.register(blood)
admin.site.register(organ)
admin.site.register(stafff)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)