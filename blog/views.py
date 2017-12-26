from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm

me = User.objects.get(username='matt')


def post_list(request):
	posts = Post.objects.all().order_by("-created_date")
	post_form = PostForm()
	return render(request, "blog/post_list.html", locals())

def add_record(request):
	if request.POST:
		title = request.POST["title"]
		text = request.POST["text"]
		newpost = Post.objects.create(author=me, title=title, text=text)
	return redirect('/blog')

def post_record(request, id):
	post = Post.objects.get(id=id)

	posts = Post.objects.filter(id__lte = id)[::-1][:2]
	post = posts[0]
	next_post = posts[1] if len(posts) > 1 else None
	
	# posts = Post.objects.all()

	# next_index = -1
	# for i, p in enumerate(posts):
	# 	if p.id == id:
	# 		next_index = i + 1

	# if next_index <= len(posts) - 1:
	# 	next_id = posts[next_index].id
	# 	next_post = Post.objects.filter(id=next_id)
	# else:
	# 	next_post = []

	return render(request, "blog/post_record.html", locals())

