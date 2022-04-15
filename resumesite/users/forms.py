from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill

class Profileform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email','username', 'password1', 'password2']

        labels = {
            'first_name': 'Имя'
        }

    def __init__(self, *args, **kwargs):
        super(Profileform, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location',
                  'bio', 'short_intro', 'profile_image', 'social_facebook',
                  'social_github', 'social_linkedin', 'social_twitter',
                  'social_youtube', 'personal_website']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name','description']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



