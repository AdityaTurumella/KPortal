from django.shortcuts import render, redirect, get_object_or_404
from classroom.models import Course, Category
from classroom.forms import NewCourseForm


def index(request):
    user = request.user
    courses = Course.objects.filter()
    context = {
        'courses':courses
    }
    return render(request,'index.html', context)

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request,'index.html', context)

def CategoryCourses(request, category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    courses = Course.objects.filter(category=category)
    context = {
        'courses':courses,
        'category':category
    }
    return render(request,'index.html', context)

def NewCourse(request):
    user = request.user
    if request.method == "POST":
        form = NewCourseForm(request.POST,request.FILES)
        if form.is_valid:
            picture = form.cleaned_data.get('picture')
            title = form.cleaned_data.get('title')
            descritpion = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            syllabus = form.cleaned_data.get('syllabus')
            Course.objects.create(picture=picture,title=title,descritpion=descritpion,category=category,syllabus=syllabus)
            return redirect('my-courses')
        else:
            form = NewCourseForm()
        context={
            'form':form
        }
        return render(request,"classroom/newcourse.html")

