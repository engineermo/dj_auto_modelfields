from django.shortcuts import render
from .models import CapUser
from django.views.generic.edit import CreateView

# Create your views here.
dia_choices = (
    ('apple', 'apple'),
    ('banane', 'banane'),
)
eda_choices = (
    ('strawberry', 'strawberry'),
    ('sanane', 'sanane'),
)


class UserCreate(CreateView):
    model = CapUser
    fields = ['current_user', ]

    def form_valid(self, form):
        form.instance.current_user = self.request.user
        if self.request.user == 'eda':
            form.instance.project_per_usr = eda_choices
        else:
            form.instance.project_per_usr = dia_choices

        return super(UserCreate, self).form_valid(form)
