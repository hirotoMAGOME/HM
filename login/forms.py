from django import forms
from django.contrib.auth.forms import UsernameField
from login.models import Member

class LoginForm(forms.Form):
    login_id = forms.CharField(
        label='ユーザー名',
        max_length=20,
    )

    password = forms.CharField(
        label = 'パスワード',
        strip=False,
        widget=forms.PasswordInput(render_value=True),
    )