from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, FileExtensionValidator


class AdvUser(AbstractUser):

    login_validator = RegexValidator(
        regex=r"^[a-zA-Z-]+$",
        message="Введите допустимое слово. Должно содержать латиницу и дефисы."
    )

    fio_validator = RegexValidator(
        regex=r"^[а-яА-Я-]+\s[а-яА-Я-]+\s[а-яА-Я-]+$",
        message="Введите допустимое слово. Должно содержать кириллицу, пробелы и дефисы"
    )

    username = models.CharField(
        verbose_name="Логин",
        max_length=150,
        unique=True,
        blank=False,
        help_text=(
            "Разрешается использовать только латиницу и дефис."
        ),
        validators=[login_validator],
        error_messages={
            "unique": "Пользователь с таким именем уже существует.",
        },
    )
    first_name = models.CharField(verbose_name="ФИО", max_length=150, blank=False, validators=[fio_validator], help_text=(
            "Разрешается использовать только кириллицу, пробелы и дефис."))
    email = models.EmailField(verbose_name="Почта", blank=False)

    last_name = None


class CategoryApplication(models.Model):
    cat_name = models.CharField(verbose_name="Категория", max_length=100, blank=False)

    def __str__(self):
        return self.cat_name


class Application(models.Model):

    date_app = models.DateTimeField(verbose_name="Временная метка", auto_now_add=True)
    name_app = models.CharField(verbose_name="Название", max_length=50, blank=False)
    desc_app = models.CharField(verbose_name="Описание", max_length=200, blank=False)
    category = models.ForeignKey(CategoryApplication, on_delete=models.CASCADE, blank=False)
    image_app = models.ImageField(verbose_name="Фотография", upload_to='images/', blank=False)
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name="Пользователь")

    STATUS_CHOICES = (
        ('Н', 'Новая'),
        ('П', 'Принята в работу'),
        ('В', 'Выполнено'),
    )

    status_app = models.CharField(verbose_name="Статус заявки", max_length=1, choices=STATUS_CHOICES, blank=False,
                                  default='Н')

    def __str__(self):
        return f"{self.name_app}, {self.category}"
