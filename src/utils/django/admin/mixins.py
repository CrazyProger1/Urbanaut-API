from django.contrib import admin


class CreatedByAdminMixin(admin.ModelAdmin):
    created_by_field: str = "created_by"

    def get_readonly_fields(self, request, obj=...):
        readonly_fields = super().get_readonly_fields(request, obj) or []

        if not request.user.is_superuser and self.created_by_field not in readonly_fields:
            return [
                self.created_by_field,
                *readonly_fields,
            ]
        return readonly_fields

    def save_model(self, request, obj, form, change):
        assert self.created_by_field, "created_by_field must be set"

        if not change and not getattr(obj, self.created_by_field, None):
            obj.created_by = request.user

        super().save_model(
            request,
            obj,
            form,
            change,
        )
