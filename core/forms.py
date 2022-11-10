from django import forms
from .models import Subscribe, Involved
from django.utils.translation import gettext as _
from django.forms import ModelForm, Select, TextInput



FORM_CHOICES= [
    ('1', 'Select the role*'),
    ('2', 'Volunteer'),
    ('3', 'Partner'),
    ('4', 'Mentor'),
    ('5', 'Donor')
    ]

class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
                                    # 'class': 'form-subs',
                                    # 'placeholder': 'Email ünvanınız',
                                    # 'id': 'value1'
                                    
                                }),
        }



class InvolvedForm(forms.ModelForm):

    class Meta:
        model = Involved
        fields = (
            'name',
            'email',
            'number',
            'membership_type',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    'placeholder': 'Name Surname*',
                                    'type': 'text'
                                }),
            'email': forms.EmailInput(attrs={
                                    'placeholder': 'E-mail address*',
                                    'type': 'email'
                                }),
            'number': forms.TextInput(attrs={
                                    'placeholder': 'Phone number*',
                                    'type': 'tel'
                                }),
            'membership_type': Select(attrs={}),
            'message': forms.Textarea(attrs={
                                    'placeholder': 'Tell us more...',
                                })
        }