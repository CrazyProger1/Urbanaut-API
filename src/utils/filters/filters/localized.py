import django_filters as filters
from django.conf import settings
from django.db.models import Q
from modeltranslation.utils import build_localized_fieldname


class LocalizedFilter(filters.CharFilter):
    def filter(self, queryset, value):
        if value in ([], (), {}, "", None):
            return queryset

        if self.distinct:
            queryset = queryset.distinct()

        query = Q()

        for lang_code, _ in settings.LANGUAGES:
            lookup = f"{build_localized_fieldname(self.field_name, lang_code)}__{self.lookup_expr}"
            query |= Q(**{lookup: value})

        return self.get_method(queryset)(query)
