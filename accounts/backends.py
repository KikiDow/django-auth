from django.contrib.auth.models import User

class EmailAuth:
    """Authenticate the user using email and password."""
    def authenticate(self, username=None, password=None):
        """Retrieve an instance of the user using email and verifying password."""
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        """Used by django authentication system to retrieve a user."""
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None