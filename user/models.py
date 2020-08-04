from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    avatar = models.ImageField('Фото', upload_to='user',blank=True,null=True)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField('Эл. почта', blank=True, null=True, unique=True)
    birthday = models.DateField('День рождения', blank=True, null=True)
    gender = models.CharField('Пол', max_length=10, blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    # def __str__(self):
    #     if self.phone:
    #         return f'{self.get_full_name()} {self.phone}'
    #     elif self.email:
    #         return f'{self.get_full_name()} {self.email}'
    #     else:
    #         return f'{self.get_full_name()} {self.id}'
    #
    # def get_user_activity(self):
    #     if (timezone.now() - self.last_activity) > dt.timedelta(seconds=10):
    #         return f'Был {self.last_activity.strftime("%d.%m.%Y,%H:%M:%S")}'
    #     else:
    #         return 'В сети'
    #
    #
    # def get_rating(self):
    #     try:
    #         return round(self.rating / self.rate_times)
    #     except:
    #         return 0
    # def get_full_name(self):
    #     if self.last_name:
    #         return f'{self.last_name} {self.first_name}'
    #     else:
    #         return f'{self.first_name}'
    #
    # def get_avatar(self):
    #     if self.avatar:
    #         return self.avatar.url
    #     elif self.photo:
    #         return self.photo
    #     else:
    #         return '/static/img/n_a.png'


# class Favorite(models.Model):
