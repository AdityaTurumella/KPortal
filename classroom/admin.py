from django.contrib import admin
from classroom.models import Course,Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Course)

