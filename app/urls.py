from xml.dom.minidom import Document
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.home.as_view(),name="home"),
    path('profile/',views.profile,name="profile"),
    path('view_profile/',views.view_profile,name="view_profile"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('address/',views.address,name="address"),
    path('offer-details/<int:pk>',views.Offer_details.as_view(),name="offer-details"),
    path('food-details/<int:pk>',views.Food_details.as_view(),name="food-details"),
    # path('customer/',views.customer ,name="customer"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    path('contact/',views.contact,name="contact"),
    path('change_password/',views.change_password.as_view(),name="change_password" ),
    path('booking/',views.ticketbookingsystem,name="booking"),
    path('delete_ticket/<int:pk>/',views.delete_ticket,name="delete_ticket"),
    path('confirm/<int:pk>/',views.confirm,name="confirm"),
    path('check_user/',views.check_user,name="check_user"),
    path('add-to-list/<int:offer_id>',views.add_to_list,name="add-to-list"),
    path('cart/',views.showcart,name="showcart"),
    path('pluscart/',views.pluscart,name="pluscart"),
    path('minuscart/',views.minuscart,name="minuscart"),
    path('removecart/',views.removecart,name="removecart"),
    path('place/',views.place,name="place"),
    # path('testpayment/',views.payment,name="testpayment")
    path('paypal/',views.paypal,name="paypal")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)