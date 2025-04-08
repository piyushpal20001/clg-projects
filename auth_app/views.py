from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book

# =============================
# 🔐 User Auth Views
# =============================

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        initial_data = {'username': '', 'password1': '', 'password2': ""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html', {'form': form})      

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        initial_data = {'username': '', 'password': ''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form': form})

def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def forgetpassword_view(request):
    forgetpassword(request)  # type: ignore
    return redirect('forget')

# =============================
# 📚 Rent Book Views
# =============================

def rent_book_view(request, books_id):
    books = Book.objects.all()
    return render(request, 'auth_app/rent_books.html', {'books': books})

@csrf_exempt  # Remove this later and use CSRF tokens in production
def rent_book(request, book_id):
    if request.method in ['POST', 'GET']:
        try:
            book = Book.objects.get(id=book_id)
            return JsonResponse({'message': f'You rented {book.name} successfully!'})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

# =============================
# 🛒 Buy Book View with Filters
# =============================

def buy_books(request):
    books = Book.objects.all()

    query = request.GET.get('q')
    category = request.GET.get('category')
    author = request.GET.get('author')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if query:
        books = books.filter(name__icontains=query)
    if category and category != 'all':
        books = books.filter(category=category)
    if author:
        books = books.filter(author__icontains=author)
    if min_price:
        books = books.filter(buy_price__gte=min_price)
    if max_price:
        books = books.filter(buy_price__lte=max_price)

    categories = Book.CATEGORY_CHOICES

    return render(request, 'buy_books.html', {
        'books': books,
        'categories': categories,
    })

# =============================
# 📤 Sell Book View with Min Price Filter
# =============================

def sell_books(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        rent_price = request.POST.get('rent_price')
        buy_price = request.POST.get('buy_price')
        category = request.POST.get('category')

        Book.objects.create(
            name=name,
            author=author,
            description=description,
            image=image,
            rent_price=rent_price,
            buy_price=buy_price,
            category=category,
        )
        return redirect('sell_books')

    min_price = request.GET.get('min_price')
    if min_price:
        books = Book.objects.filter(buy_price__gte=min_price)
    else:
        books = Book.objects.all()

    return render(request, 'sell_books.html', {
        'books': books,
        'min_price': min_price or ''
    })

# =============================
# 🛍 Shop Now Page with Full Filters
# =============================

def shop_now(request):
    books = Book.objects.all()

    query = request.GET.get('q')
    category = request.GET.get('category')
    author = request.GET.get('author')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if query:
        books = books.filter(name__icontains=query)
    if category and category != 'all':
        books = books.filter(category=category)
    if author:
        books = books.filter(author__icontains=author)
    if min_price:
        books = books.filter(buy_price__gte=min_price)
    if max_price:
        books = books.filter(buy_price__lte=max_price)

    categories = Book.CATEGORY_CHOICES

    return render(request, 'shop_now.html', {
        'books': books,
        'categories': categories,
})