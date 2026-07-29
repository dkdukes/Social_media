from django import forms
from .models import CustomUser,Tags, Posts
from django.contrib.auth import get_user_model


User = get_user_model()
class UserForm(forms.ModelForm):
    username = forms.CharField(required=False, validators=[],help_text="",widget=forms.TextInput(attrs={
        'class':"border rounded-sm mb-4 p-2 w-1/4",
        'placeholder':'Your username'
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-1/4 rounded-sm p-2"
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-1/4 rounded-sm p-2"
        })
    )
    class Meta:
        model = CustomUser
        fields = ["first_name","last_name","username","password","email","bio","image"]
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match!")
            return cleaned_data
        
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


