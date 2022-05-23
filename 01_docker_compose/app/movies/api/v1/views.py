from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.db.models import F, Q
from movies.models import Filmwork, Role
from django.contrib.postgres.aggregates import ArrayAgg


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        return self.model.objects.all().select_related('person', 'genres').values(
            'id',
            'title',
            'description',
            'creation_date',
            'rating',
            'type'
            ).annotate(
                genres=ArrayAgg(F('genres__name'), distinct=True),
                actors=ArrayAgg(F('person__full_name'), distinct=True, filter=Q(personfilmwork__role=Role.ACTOR)),
                directors=ArrayAgg(F('person__full_name'), distinct=True, filter=Q(personfilmwork__role=Role.DIRECTOR)),
                writers=ArrayAgg(F('person__full_name'), distinct=True, filter=Q(personfilmwork__role=Role.SCREENWRITER))
            )
    
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(page.object_list),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context['object']