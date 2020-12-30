from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'body', 'created', 'active')
    list_filter = ('active', 'created', 'organization')
    search_fields = ('name', 'organization', 'body')
    date_hierarchy = 'created'
    ordering = ('created', 'active')
