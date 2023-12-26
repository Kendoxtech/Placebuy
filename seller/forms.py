from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match')
        return cd['password2']
    

class CustomPasswordChangeForm(PasswordChangeForm):
    # You can customize the form fields or add extra validations if needed
    # For example, you can add a new password confirmation field
    new_password_confirmation = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='New Password Confirmation'
    )

    def clean_new_password_confirmation(self):
        # Validate that the new password and confirmation match
        new_password = self.cleaned_data.get('new_password1')
        new_password_confirmation = self.cleaned_data.get('new_password_confirmation')

        if new_password and new_password_confirmation and new_password != new_password_confirmation:
            raise forms.ValidationError("The new password and confirmation do not match.")

        return new_password_confirmation
