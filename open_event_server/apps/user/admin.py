from django.contrib import admin

from open_event_server.apps.user.models import User, ActionToken

admin.site.register(User)
admin.site.register(ActionToken)
