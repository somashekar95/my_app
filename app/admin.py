from django.contrib import admin
from .models import App,User,TaskCompletion

# Register your models here
admin.site.register(App)
admin.site.register(User)
admin.site.register(TaskCompletion)