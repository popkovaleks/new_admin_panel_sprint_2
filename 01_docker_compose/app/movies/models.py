import uuid


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _



class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):

    name = models.CharField(_('name'), max_length=255)

    description = models.TextField(_('description'), blank=True)

    class Meta:
        db_table = "content\".\"genre"

        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

        indexes = [
            models.Index(fields=['name'], name='genre_name_idx')
        ]

    def __str__(self):
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):

    title = models.CharField(_('title'), max_length=255)

    description = models.TextField(_('description'), blank=True)

    creation_date = models.DateField(_('creation date'), blank=True)

    rating = models.FloatField(_('rating'), blank=True, validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(10)
                                                        ])

    class FilmworkType(models.TextChoices):
        MOVIE = 'M', _('Movie')
        TV_SHOW = 'TV', _('TV show')

    type = models.CharField(
        _('type'),
        max_length=2,
        choices=FilmworkType.choices)

    genres = models.ManyToManyField(Genre, through='GenreFilmwork')

    class Meta:
        db_table = "content\".\"film_work"

        verbose_name = "Кинопроизведение"
        verbose_name_plural = "Кинопроизведения"

        indexes = [
            models.Index(fields=['creation_date'], name='film_work_creation_date_idx')
        ]

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)

    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"

        verbose_name = _('Genre Filmwork')
        verbose_name_plural = _('Genres Filmworks')

        constraints = [
            models.UniqueConstraint(fields=['film_work', 'genre'], name='genre_film_work_idx')
        ]


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.TextField(_("full name"))
    birth_date = models.DateField(_("birthday"), blank=True)
    film_work = models.ManyToManyField(Filmwork, through='PersonFilmwork')

    class Meta:
        db_table = "content\".\"person"

        verbose_name = "Человек"
        verbose_name_plural = "Люди"

        indexes = [
            models.Index(fields=['full_name'], name='person_full_name_idx')
        ]

    def __str__(self):
        return self.full_name


class Role(models.TextChoices):
        DIRECTOR = 'Dir', _('Director')
        SCREENWRITER = 'ScrWrtr', _('Screenwriter')
        ACTOR = 'Act', _('Actor')


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)

    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    role = models.CharField(_('role'),
                            null=True,
                            max_length=7,
                            choices=Role.choices)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"

        verbose_name = _('person of filmwork')
        verbose_name_plural = _('persons of filmwork')

        constraints = [
            models.UniqueConstraint(fields=['film_work', 'person'], name='person_full_name_idx')
        ]
