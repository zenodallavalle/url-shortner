from django.contrib import admin

# Register your models here.

from main.models import UrlShortner, Visit


class UrlShortnerAdmin(admin.ModelAdmin):
    list_display = ("user", "created", "edit", "url", "short_url")
    list_filter = ("user", "created", "edit")
    search_fields = ("user", "url", "short_url")
    readonly_fields = ("n_visits", "created", "edit", "last_visit", "short_url")


class VisitAdmin(admin.ModelAdmin):
    readonly_fields = (
        "url",
        "datetime",
    )


admin.site.register(UrlShortner, UrlShortnerAdmin)
admin.site.register(Visit, VisitAdmin)
