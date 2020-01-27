from django.contrib import admin

# Register your models here.
from .models import CapUser

dia_choices = [
    ('apple', 'apple'),
    ('banane', 'banane'),
]

eda_choices = [
    ('strawberry', 'strawberry'),
    ('sanane', 'sanane'),
]


class CapUserAdmin(admin.ModelAdmin):
    # readonly_fields = ('current_user',)
    list_display = ['get_current_user', ]

    def get_current_user(self, obj):
        if obj.user is not None:
            return obj.user.username
        return '-'

    get_current_user.short_description = 'Current User'

    # def save_model(self, request, obj, form, change):
    #     if not obj.current_user:
    #         obj.current_user = request.user
    #     obj.save()

    def get_changeform_initial_data(self, request):
        get_data = super(CapUserAdmin, self).get_changeform_initial_data(request)
        get_data['current_user'] = request.user
        # if get_data['current_user'] == 'eda' or 'EDA':
        #     get_data['project_per_usr'] = eda_choices
        #     return get_data
        return get_data


admin.site.register(CapUser, CapUserAdmin)
