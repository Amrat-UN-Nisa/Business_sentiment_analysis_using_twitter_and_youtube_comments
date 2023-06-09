from django import forms

from sentiment.models import User


class InputTextForm(forms.Form):
    input_url = forms.CharField(
        min_length=10, max_length=150,
        widget=forms.TextInput(
            {
                'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-transparent focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-ou',
                'placeholder': "Enter URL for youtube"
            }
        )
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        min_length=6, max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    password = forms.CharField(
        min_length=6, max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )


class BasicRegForm(forms.ModelForm):
    username = forms.CharField(
        min_length=4, max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'})
    )
    email = forms.EmailField(
        min_length=6, max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    password = forms.CharField(
        min_length=6, max_length=20,
        widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("password does not matched")
        return password
