from django.urls import path
from . import views
from .views import rent_book_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Auth Views
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('forget-password/', views.forgetpassword_view, name='forget_password'),

    # Password Reset Views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Rent Book URLs
    path('auth/rent-book/<int:book_id>/', views.rent_book, name='rent_book_api'),
    path('rent-books/', rent_book_view, name='rent_book'),

    # Buy Books Page
    path('buy-books/', views.buy_books, name='buy_books'),

    # Sell Books Page (💰 filter by min_price)
    path('sell-books/', views.sell_books, name='sell_books'),

    # Shop Now Page (🛍 main public view with all filters)
    path('shop-now/', views.shop_now, name='shop_now'),
]