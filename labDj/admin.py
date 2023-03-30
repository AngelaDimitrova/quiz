from datetime import datetime
from django.contrib import admin
from labDj.models import *
from rangefilter.filters import DateRangeFilter


class SkillsAdmin(admin.StackedInline):
    model = Skills
    extra = 0


class InterestsAdmin(admin.StackedInline):
    model = Interest
    extra = 0


class UserModelAdmin(admin.ModelAdmin):
    list_display = ("get_username", "get_first_name", "get_last_name", "get_email")
    inlines = [SkillsAdmin, InterestsAdmin]

    def get_first_name(self, obj):
        return obj.user_model.first_name

    def get_last_name(self, obj):
        return obj.user_model.last_name

    def get_username(self, obj):
        return obj.user_model.username

    def get_email(self, obj):
        return obj.user_model.email

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or (obj and obj.user_model == request.user):
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or (obj and obj.user_model == request.user):
            return True
        else:
            return False


admin.site.register(UserModel, UserModelAdmin)


class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]
    list_display = ("title", "author")
    list_filter = (('pub_date', DateRangeFilter),)
    search_fields = ("title", "desc")
    exclude = ("author", "change_date", "pub_date")

    def save_model(self, request, obj, form, change):
        obj.author = UserModel.objects.filter(user_model=request.user).get()
        obj.change_date = datetime.now()
        if obj and not obj.pub_date:
            obj.pub_date = datetime.now()
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.author.user_model or request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.author.user_model or request.user.is_superuser:
            return True
        else:
            return False

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True

        for block_list in [blockedUser for blockedUser in BlockedList.objects.filter(user_blocking=obj.author)]:
            if block_list.user_blocked.user_model == request.user:
                return False
        return True


admin.site.register(Post, PostAdmin)


class BlockedListAdmin(admin.ModelAdmin):
    exclude = ("user_blocking",)

    def save_model(self, request, obj, form, change):
        obj.user_blocking = UserModel.objects.filter(user_model=request.user).get()
        super().save_model(request, obj, form, change)


admin.site.register(BlockedList, BlockedListAdmin)
