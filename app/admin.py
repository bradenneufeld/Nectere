from django.contrib import admin
from app.models import User, MFilter, UserMatchMeta, UserSelfMeta, MFilterOptions


class MFilterOptionsInline(admin.TabularInline):
    model = MFilterOptions
    extra = 1


class UserMatchMetaInline(admin.TabularInline):
    readonly_fields = ['m_filter']
    model = UserMatchMeta
    extra = 1


class UserSelfMetaInline(admin.TabularInline):
    model = UserSelfMeta
    extra = 1


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    inlines = [UserSelfMetaInline, UserMatchMetaInline]


class MFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    inlines = [MFilterOptionsInline]



# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(MFilter, MFilterAdmin)