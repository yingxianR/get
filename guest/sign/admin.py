from django.contrib import admin
from sign.models import Event, Guest
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = ['name','status','start_time','id']

class GuestAdmin(admin.ModelAdmin):
	list_display = ['realname','phone','email']

admin.site.register(Event)
admin.site.register(Guest)

