from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book, Author

# Create your views here.
    
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            errors.append('No author matched your search criteria.')
            authors = Author.objects.filter(Name=q)
            for author in authors:
                author_id = author.AuthorID
                books = Book.objects.filter(AuthorID=author_id)
                return render_to_response('search_results.html',
                                {'books': books, 'query': q, 'author': author})
                            
    return render_to_response('search.html', {'errors': errors})
    
def show(request, isbn):
    bk = Book.objects.get(ISBN = isbn)
    bk_id = bk.AuthorID
    au = Author.objects.get(AuthorID=bk_id)
    return render_to_response('show_book.html', {'bk': bk, 'au': au})
    
def delete(request, isbn):
    bk = Book.objects.get(ISBN = isbn)
    bk.delete()
    Book_list = Book.objects.order_by('Title')
    Author_list = Author.objects.order_by('Name')
    return render_to_response('home.html', {'Book_list': Book_list, 'Author_list': Author_list})
    
def home(request):
    Book_list = Book.objects.order_by('Title')
    Author_list = Author.objects.order_by('Name')
    return render_to_response('home.html', {'Book_list': Book_list, 'Author_list': Author_list})
    
def alista():
    return a
    
    
    
    
    
    
    
    
    
