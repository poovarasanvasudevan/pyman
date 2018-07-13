from django.contrib import admin

# Register your c_models here.
from django.contrib.admin.models import LogEntry
from kernel.log.log_entry_admin import LogEntryAdmin

admin.site.register(LogEntry, LogEntryAdmin)