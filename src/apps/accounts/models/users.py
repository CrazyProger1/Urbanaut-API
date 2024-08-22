from django.contrib.auth.models import PermissionsMixin, AbstractUser


class User(AbstractUser, PermissionsMixin):
    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
