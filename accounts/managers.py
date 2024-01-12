from django.contrib.auth.models import BaseUserManager
from django.db.models import Q


class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

    def users(self, user=None, include_superuser=False):
        if user:
            filter_dict = {}
            filter_q = Q()

            if not include_superuser:
                filter_q = ~Q(is_superuser=True)

            if user.is_superuser:
                pass
            elif user.is_admin:
                filter_dict = {"company__in": user.companies.all()}
            elif user.is_manager:
                filter_dict.update({"company": user.company})
            elif user.is_hod:
                filter_dict.update({'site__in': user.sites.all()})
            else:
                return self.none()

            return self.filter(filter_q, **filter_dict)

        else:
            return self.none()
