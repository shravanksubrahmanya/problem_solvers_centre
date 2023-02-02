from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserManager(BaseUserManager):
    def create_user(self, user_type, account_type, email, password):
        if not email:
            raise ValueError('User must provide valis email address')
        if not password:
            raise ValueError('User must provide password')
        
        user = self.model(
            user_type = user_type,
            account_type = account_type,
            email = self.normalize_email(email=email) # it normalizes the email for storage
        )

        user.set_password(raw_password = password) # it hashes password before setting it up into the database
        user.save(using = self._db)
        return user

    
    def create_superuser(self, user_type, account_type, email, password):
        user = self.create_user(
            user_type= user_type,
            account_type= account_type,
            email=email, 
            password= password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user