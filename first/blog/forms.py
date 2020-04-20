from django import forms

class CommentForm(forms.Form):
	author = forms.CharField(max_length=60)
	body = forms.CharField(widget=forms.Textarea())