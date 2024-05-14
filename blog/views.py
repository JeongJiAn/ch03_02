from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def practice2(request):
    return render(request, 'blog/practice2.html', {})