from django.contrib import admin
from .models import ColourCategory, AnimalCategory, CollarCategory, Listing, Sighting


class ColourCategoryAdmin(admin.ModelAdmin):
    pass


class AnimalCategoryAdmin(admin.ModelAdmin):
    pass


class CollarCategoryAdmin(admin.ModelAdmin):
    pass


class ListingAdmin(admin.ModelAdmin):
    pass


class SightingAdmin(admin.ModelAdmin):
    pass


admin.site.register(ColourCategory, ColourCategoryAdmin)
admin.site.register(AnimalCategory, AnimalCategoryAdmin)
admin.site.register(CollarCategory, CollarCategoryAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Sighting, SightingAdmin)
