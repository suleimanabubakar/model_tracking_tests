from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.


class TicketHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id",  "name","history"]
    history_list_display = ["name"]
    search_fields = ['name', 'user__username']

admin.site.register(Ticket, TicketHistoryAdmin)



admin.site.register(Student)
admin.site.register(Teacher)