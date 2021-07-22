from django import forms
from django.forms import fields, widgets
from .models import Comment, Post,Category 

choices=Category.objects.all().values_list('name','name')
choice_list=[]
for i in choices:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','title_tag','author','category','body', 'header_image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder','type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','title_tag','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }        

class AddCommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }                