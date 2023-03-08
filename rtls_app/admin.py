from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Module)
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Asset)
admin.site.register(Stock)
admin.site.register(Vehicle)
admin.site.register(Location)
admin.site.register(Zone)
admin.site.register(Floor)
admin.site.register(Building)
admin.site.register(Unit)
admin.site.register(Inventory)
admin.site.register(Task)
admin.site.register(TaskResponsible)
admin.site.register(Enumeration)
admin.site.register(EnumerationType)
admin.site.register(User)

admin.site.register(TagPosition)


