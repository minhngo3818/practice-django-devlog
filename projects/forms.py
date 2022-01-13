from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'  # add all fields in modelfrom
        exclude = ['vote_total', 'vote_ratio']

