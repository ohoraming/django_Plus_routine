from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class SigninForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = [
            'email',
            'password',
        ]
        
class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
