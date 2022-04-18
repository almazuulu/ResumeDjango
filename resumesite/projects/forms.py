from .models import *
from django.forms import ModelForm
from django import forms

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags','featured_image']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input'})
        #
        # self.fields['description'].widget.attrs.update({'class': 'input'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Проголсуйте здесь',
            'body': 'Прокомментируйте здесь'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


