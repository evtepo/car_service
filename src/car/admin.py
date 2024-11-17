from django.contrib import admin

from car.models import Car, Comment


class AdminMixin(admin.ModelAdmin):
    show_full_result_count = False

    class Meta:
        abstract = True


@admin.register(Car)
class CarAdmin(AdminMixin):
    list_display = ("make", "model", "year", "description", "created_at", "updated_at", "owner")
    list_filter = ("make", "owner")

    def changed_description(self, obj):
        description = obj.description
        return description[:40] + "..." if len(description) > 40 else description

    changed_description.short_description = "Описание автомобиля"


@admin.register(Comment)
class CommentAdmin(AdminMixin):
    list_display = ("author", "car", "changed_content", "created_at")

    def changed_content(self, obj):
        content = obj.content
        return content[:40] + "..." if len(content) > 40 else content

    changed_content.short_description = "Содержание комментария"
