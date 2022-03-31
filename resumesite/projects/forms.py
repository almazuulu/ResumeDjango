from .models import *
from django.forms import ModelForm

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']

