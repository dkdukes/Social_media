from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()
class RoleAssignmentForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required= False,
        widget= forms.CheckboxSelectMultiple,
        label= "Roles(Groups)",
        help_text="select one or more roles for this user"
    )
    class Meta:
        model=User
        fields=["email","first_name","last_name","groups"]
        widgets={
            "email":forms.EmailInput(attrs={
                "readonly":"readonly",
                "class":"bg-gray-100"
            })
        }
        help_texts={
            "first_name":"Optional:users first name",
            "last_name":"Optional: users last name"
        }