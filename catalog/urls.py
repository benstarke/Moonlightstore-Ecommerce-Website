
from django.urls import path,include
from .views import *
from . import views


urlpatterns = [
	#path('',HomeView.as_view(),name='hom10e'),
	#path('product/<slug>',ProductDetail.as_view(),name='product'),
	path('abouts/',views.abouts,name='abouts'),
	path('product/<slug>/',views.product,name='product'),
	path('', views.home, name='home'),
	path('product-list/',views.product_list,name='product_list'),
	path('checkout/',checkout,name='checkout'),
	path('contact/',contact,name='contact'),
	path('add_to_cart/<slug>/',add_to_cart,name='add_to_cart'),
	path('order_summary/',OrderSummaryView.as_view(),name='order_summary'),
	path('delivery/',delivery, name='delivery'),
	path('remove_from_cart/<slug>/',remove_from_cart,name='remove_from_cart'),
	path('search/', SearchResultsView.as_view(), name='search_results'),
	# path('signup/',views.signup,name='signup'),
	path('register/',views.register,name='register'),
	path('login/',views.logins,name='login'),
	#path('accounts/',include('django.contrib.auth.urls')),
	path('help', views.help, name='help'),
	path('promotion', views.promotion, name='promotion'),
	#wish list
	path('wishlist/',views.wishlist,name='wishlist'),
	path('wishlist/add_to_wishlist/<int:id>',views.add_to_wishlist,name='add_to_wishlist'),
]