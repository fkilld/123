from django.contrib import admin
from main.models import *


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'stream', 'phone', 'date_joined')
    list_display_links = ('first_name', 'email', 'stream', 'phone')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone','date_of_contact')
    list_display_links = ('full_name', 'email', 'phone',)


class Tap_modelAdmin(admin.ModelAdmin):
    list_display = ('job_title',)
    list_display_links = ('job_title',)


class FullStackAdmin(admin.ModelAdmin):
    list_display = ('fname', 'femails', 'fphones', 'upcomingBatch','date_full')
    list_display_links = ('fname', 'femails', 'fphones', 'upcomingBatch',)


class DigitalMarketAdmin(admin.ModelAdmin):
    list_display = ('fname', 'femails', 'fphones','date_market')
    list_display_links = ('fname', 'femails', 'fphones',)


admin.site.register(Register, RegisterAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tap_model, Tap_modelAdmin)
admin.site.register(FullStack, FullStackAdmin)
admin.site.register(DigitalMarket, DigitalMarketAdmin)
