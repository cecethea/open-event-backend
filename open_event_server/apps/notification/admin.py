from django.contrib import admin

from open_event_server.apps.notification.models import (
    Notification
)

admin.site.register(Notification)
