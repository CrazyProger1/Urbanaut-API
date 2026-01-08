from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_oauth_user(self, email: str, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.save()
        return user

    def create_user(self, password: str = None, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password: str = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(password, **extra_fields)
