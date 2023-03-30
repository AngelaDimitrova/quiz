import django.contrib.auth.models
from django.db import models


class UserModel(models.Model):
    user_model = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pictures", blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user_model.first_name + " " + self.user_model.last_name + " " + self.user_model.email


class Skills(models.Model):
    skill = models.CharField(max_length=30)
    skill_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.skill


class Interest(models.Model):
    interest = models.CharField(max_length=30)
    interest_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.interest


class BlockedList(models.Model):
    user_blocked = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_blocked')
    user_blocking = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_blocking')

    def __str__(self):
        return self.user_blocked.user_model.first_name + " " + self.user_blocked.user_model.last_name + " " + \
               self.user_blocked.user_model.email


class Post(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish_date')
    change_date = models.DateTimeField('change_date')
    file = models.FileField(upload_to="post_pictures", blank=True, null=True)

    def __str__(self):
        return self.title + " " + str(self.author.user_model)


class Comment(models.Model):
    comment_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.content


# Create your models here.
