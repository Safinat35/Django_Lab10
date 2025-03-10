from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#    name = request.GET.get("name") or "world!"
#    return render(request, "bookmodule/index.html" , {"name": name})  
   
# def index2(request, val1=None):  
#    try:
   
#       val1 = int(val1)
#    except (ValueError, TypeError):
   
#       return HttpResponse("Error, expected val1 to be integer")

#    return HttpResponse(f"value1 = {val1}")

# def viewbook(request, bookId):
#    # assume that we have the following books somewhere (e.g. database)
#    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
#    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
#    targetBook = None
#    if book1['id'] == bookId: targetBook = book1
#    if book2['id'] == bookId: targetBook = book2
#    context = {'book':targetBook} # book is the variable name accessible by the template
#    return render(request, 'bookmodule/show.html', context)

# def index(request):
#    return render(request, "bookmodule/index.html")

# def list_books(request):
#    return render(request, 'bookmodule/list_books.html')

# def viewbook(request, bookId):
#    return render(request, 'bookmodule/one_book.html')

# def aboutus(request):
#    return render(request, 'bookmodule/aboutus.html')


def home(request):
   return HttpResponse("<h1>Welcome to the Library Project</h1><p>Go to <a href='/books/html5/links/'>Links Page</a></p>")


def index(request):
   return render(request, "bookmodule/index.html")

def list_books(request):
   return render(request, 'bookmodule/list_books.html')

def aboutus(request):
   return render(request, 'bookmodule/aboutus.html')

def viewbook(request, bookId):
   return render(request, 'bookmodule/one_book.html')



def search(request):
   if request.method == "POST":
      string = request.POST.get('keyword').lower()
      isTitle = request.POST.get('option1')
      isAuthor = request.POST.get('option2')
      # now filter
      books = __getBooksList()
      newBooks = []
      for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
      return render(request, 'bookmodule/bookList.html', {'books':newBooks})
   return render(request, 'bookmodule/search.html')

def __getBooksList():
   book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
   book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
   book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
   return [book1, book2, book3]

def filterbooks(request):
# have fake books:
   book1 = {'id':12344321,'title':'Continuous Delivery','author':'J.Humble and D. Farley'}
   book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering','author':'E. Eilam'}
   book3 = {'id':43211234,'title':'The Hundred-Page Machine Learning Book','author':'Andriy Burkov'}
   
   books=[]
   books.append(book1)
   books.append(book2)
   books.append(book3)
   
   return render(request, 'bookmodule/search.html', {})
