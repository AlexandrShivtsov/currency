from currency.models import ContactCreate, Source

from django.contrib import admin


class ContactCreateAdmin(admin.ModelAdmin):
    list_display = (
        'email_to',
        'subject',
        'message',
        'created'
    )

    list_filter = (
        'created',
    )

    search_fields = (
        'subject',
    )

    readonly_fields = (
        'email_to',
        'subject',
        'message',
        'created',
    )

    def has_delete_permission(self, request, obj=None):
        return None


admin.site.register(ContactCreate, ContactCreateAdmin)


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'source_url',
        'name',
    )


admin.site.register(Source, SourceAdmin)
