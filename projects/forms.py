from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'src_link']  # add all fields in modelfrom

        # Create a check box style for tags
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

# Re-modify field to render each object of tags
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})