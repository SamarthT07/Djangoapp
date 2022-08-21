from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name', 'last_name','email']
        labels={'first_name':'ur_first_name','last_name':'ur_last_name','email':'email'}

class edituserform(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields=['username','first_name','last_name', 'email', 'date_joined', 'last_login',]

class editadminform(UserChangeForm):
        password = None
        class Meta:
            model=User
            fields='__all__'
class mysetpasswordform(SetPasswordForm):
    class Meta:
        model=User
        fields='__all__'