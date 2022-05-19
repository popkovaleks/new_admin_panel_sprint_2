from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Genre, Filmwork, Person, GenreFilmwork, PersonFilmwork


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

    search_fields = ('id', 'name',)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline)

    list_display = ('title', 'type', 'creation_date', 'rating', 'get_genres')

    list_filter = ('type',)

    search_fields = ('title', 'description', 'id', )

    list_prefetch_related = ('genres',)
    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .prefetch_related(*self.list_prefetch_related)
        )
        return queryset

    def get_genres(self, obj):
        return ','.join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = _('Film genres')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

    search_fields = ('id', 'full_name',)
