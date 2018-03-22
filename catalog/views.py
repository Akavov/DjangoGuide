from django.shortcuts import render

# Create your views here.
from .models import Book,Author,BookInstance,Genre

def index(request):
    """
    Mapping function for home page
    """
    #Generation some main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    #Available books
    num_instances_available=BookInstance.objects.filter(status='a').count()
    num_authors=Author.objects.count() #Method 'all()' has used by default

    #Number of visits to this view , as counted in the session variable.
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1
    #Rendering HTML index.html with data
    #in var context
    return render(
        request,'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_visits':num_visits},
    )

from django.views import generic

class BookListView(generic.ListView):
    model=Book
    paginate_by=10
    #context_object_name='my_book_list' # our own name of context var in template
    #queryset=Book.objects.filter(title='war')[:5] # taking 5 books with 'war' in the title
    #template_name='books/my_arbitrary_template_name_list.html' #referencing template name and its location

class BookDetailView(generic.DetailView):
    model=Book
