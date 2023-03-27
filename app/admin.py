from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,  Base, Command, Brigade, Battalion, Company


admin.site.register(User, UserAdmin)

# Register your models here.
#admin.site.register(Base)
#admin.site.register(Command)
#admin.site.register(Brigade)
#admin.site.register(Battalion)
#admin.site.register(Company)

class BaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Base, BaseAdmin)

class CommandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Command, CommandAdmin)

class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('name', 'command')

admin.site.register(Brigade, BrigadeAdmin)

class BattalionAdmin(admin.ModelAdmin):
    list_display = ('name', 'brigade')

admin.site.register(Battalion, BattalionAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'battalion')

admin.site.register(Company, CompanyAdmin)