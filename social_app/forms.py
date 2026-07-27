from django import forms
from .models import CustomUser,Tags, Posts

class UserForm(forms.ModelForm):
    username = forms.CharField(required=False, validators=[],help_text="",widget=forms.TextInput(attrs={
        'class':"border rounded-sm mb-4 p-2 w-1/4",
        'placeholder':'Your username'
    }))
    class Meta:
        model = CustomUser
        fields = ["first_name","last_name","username","email","bio","image"]
        widgets={
            'first_name':forms.TextInput(attrs={
                'class':"border rounded-sm mb-4 p-2 w-1/4",
                'placeholder':"Your first name"
            }),
            'last_name':forms.TextInput(attrs={
                'class':"border rounded-sm mb-4 p-2 w-1/4",
                'placeholder':"Your last name"
            }),
            'email':forms.EmailInput(attrs={
                'class':"border rounded-sm mb-4 p-2 w-1/4",
                'placeholder':"Your email"
            }),
            'bio':forms.Textarea(attrs={
                'class':"border rounded-sm mb-4 p-2 w-1/4",
                'placeholder':"Your bio"
            }),
            'image':forms.ClearableFileInput(attrs={
                'class':"border rounded-sm mb-4"
            })
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tags']
        widgets = {
            'tags':forms.TextInput(attrs={
                'class':"border rounded-sm mb-4 p-2 w-1/4",
                'placeholder':"Enter a tag"
            })
        }


class PostForm(forms.ModelForm):
    class Meta:
        VISIBILITY_CHOICES = [
                ('public','Public'),
                ('private','Private')
            ]
        visibility = forms.ChoiceField(
            choices=VISIBILITY_CHOICES,
            label="Post Visibility"
        )
        model = Posts
        fields = ['caption','image','location','visibility','tags']
        widgets = {
            'caption':forms.Textarea(attrs={
                'class':"border rounded-sm mb-4 w-1/4",
                'placeholder':"Post caption"
            }),
            'image':forms.ClearableFileInput(attrs={
                'class':"border rounded-sm mb-4"
            }),
            'location':forms.TextInput(attrs={
                'class':"border rounded-sm mb-4 w-1/4",
                'placeholder':"Your location"
            }),
            'tags':forms.SelectMultiple(attrs={
                'class':"border rounded-sm p-2 w-1/4"
            })
        }
    