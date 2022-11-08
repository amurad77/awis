from django import forms
from .models import Subscribe
from django.utils.translation import gettext as _


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