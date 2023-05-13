from django.contrib.auth import get_user_model #imports custom user which looks to AUTH_USER_MODELS in settings.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        models = get_user_model
        fields = ('email', 'username',) # PAssword field is explicitly added so need adding it here


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        models = get_user_model
        fields = ('email', 'username',) # PAssword field is explicitly added so need adding it here
        