from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Profileform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email','username', 'password1', 'password2']

        labels = {
            'first_name': 'Имя'
        }

    def __init__(self, *args, **kwargs):
        super(Profileform, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input'})
        #
        # self.fields['description'].widget.attrs.update({'class': 'input'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})