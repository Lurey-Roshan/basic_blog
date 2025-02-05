import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import NoReverseMatch, reverse
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm
# Create your views here.
from blog.models import Post, Comments,Category
def blog_index(request):
	posts = Post.objects.all().order_by('-created_on')
	context = {
	'posts': posts
	}
	return render(request, 'blogs/blog_index.html', context)

def blog_category(request, category):
	posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
	context = {
		'category': category,
		'posts': posts
		}
	return render(request, 'blogs/blog_category.html', context)

def blog_detail(request, pk):
	post = Post.objects.get(pk=pk)
	form=CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment=Comments(
				author=form.cleaned_data['author'],
				body=form.cleaned_data['body'],
				post=post
				)
			comment.save()
			form = CommentForm()
	comments = Comments.objects.filter(post=post)
	context = {
		'form':form,
		'post': post,
		'comments': comments,
		}
	return render(request, 'blogs/blog_detail.html', context)

