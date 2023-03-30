from django.shortcuts import render, redirect
from labDj.models import Post, UserModel, BlockedList, Skills, Interest
from .forms import PostForm, BlockedListForm
from datetime import datetime


def posts(request):
    blocked = BlockedList.objects.filter(user_blocking__user_model=request.user)
    block_list = [b.user_blocked.user_model for b in blocked]
    print(block_list)
    queryset = Post.objects.exclude(author__user_model=request.user).exclude(author__user_model__in=block_list)
    context = {"posts": queryset}
    return render(request, 'posts.html', context=context)


def profile(request):
    querysetSkills = Skills.objects.filter(skill_user__user_model=request.user)
    querysetInterests = Interest.objects.filter(interest_user__user_model=request.user)
    queryset = UserModel.objects.filter(user_model=request.user)
    querysetposts = Post.objects.filter(author__user_model=request.user)
    context = {"userSkills": querysetSkills, "userInterests": querysetInterests, "user_info": queryset,
               "user_posts": querysetposts}
    return render(request, "profile.html", context=context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = UserModel.objects.filter(user_model=request.user).get()
            post.pub_date = datetime.now()
            post.change_date = datetime.now()
            post.save()
            return redirect("profile")
    context = {"form": PostForm}
    return render(request, "add_post.html", context=context)


def blocked_users(request):
    if request.method == "POST":
        form = BlockedListForm(request.POST)
        if form.is_valid():
            blist = form.save(commit=False)
            blist.user_blocking = UserModel.objects.filter(user_model=request.user).get()
            blist.save()
            return redirect("blocked_users")
    queryset = BlockedList.objects.filter(user_blocking__user_model=request.user)
    context = {"blocked": queryset, "form": BlockedListForm}
    return render(request, "blocked_users.html", context=context)