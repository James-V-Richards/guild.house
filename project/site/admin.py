# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .forms import HomepageAdminForm
from .models import Homepage
from django.contrib import admin


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Content', {'fields': ['title', 'heading', 'featured_content',
                                'content', 'meta_description']}),
        ('Publishing', {'fields': ['is_enabled', 'site',
                                   ('created_at', 'updated_at')],
                        'classes': ['collapse']}),
    ]

    form = HomepageAdminForm

    list_display = ['__str__', 'is_active']

    readonly_fields = ['created_at', 'updated_at']
