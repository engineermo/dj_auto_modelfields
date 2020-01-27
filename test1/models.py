from django.contrib.auth.models import User
from django.db import models

eda_choices = [
    ('strawberry', 'strawberry'),
    ('sanane', 'sanane'),
]


def get_choices():
    choices = []
    if CapUser.current_user == 'eda' or 'EDA':
        choices = eda_choices
    return choices


# Create your models here.
class CapUser(models.Model):
    current_user = models.CharField(max_length=200, help_text='The current user will be retrieved and put in this box')
    project_per_usr = models.CharField(max_length=100, choices='', help_text="projects based on current user",
                                       blank=True)

    def __str__(self):
        return self.current_user

    def __init__(self, *args, **kwargs):
        super(CapUser, self).__init__(*args, **kwargs)
        self._meta.get_fields()[2].choices = get_choices()

"""
try doing this in the Admin
"""