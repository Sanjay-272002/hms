from django.contrib import admin
from django.urls import path
from  .import views
from django.contrib.auth.views import LoginView,LogoutView

from .import views
# urls for admin
urlpatterns= [
    path('',views.home_view,name='home'),
    path('signup',views.signup_view,name="signup"),
    path('adminsignup', views.admin_signup_view),
    path('staffsignup', views.staff_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    path('login',LoginView.as_view(template_name='login.html')),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('aboutus',views.aboutus_view),
    path('contactus',views.contactus_view),
    path('weather',views.weather_view),
    path('blood_view',views.blood_view,name="blood_view"),
    path('med',views.med_view,name='med'),
    path('organ',views.organ_view,name='organ'),        
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),

    #lab
    path('staffdash', views.staff_dashboard_view,name='staffdash'),
    path('upload/<int:pk>', views.staff_upload_view,name='upload'),
    path('details', views.staff_details_view,name='details'),
    path('cart', views.cart_view,name='cart'),

 #admin-doctor
    path('admindash', views.admin_dashboard_view,name='admindash'),
    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),

    #admin-patient
    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),

    #admin-appointment
    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
   
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
    path('admin-approve-bed', views.admin_approve_bed_view,name='admin-approve-bed'),
    path('approve-bed/<int:pk>', views.approve_bed_view,name='approve-bed'),
    path('reject-bed/<int:pk>', views.reject_bed_view,name='reject-bed'),

    path('adminbbed', views.admin_view_bed_view,name='adminbbed'),
#admin url ends


    #doctorpage urls
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctordash'),
    path('search', views.search_view,name='search'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),

    path('patient-dashboard', views.patient_dashboard_view,name='patientdash'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-book-bed', views.patient_book_bed_view,name='patient-book-bed'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-view-bed', views.patient_view_bed_view,name='patient-view-bed'),
    path('patient-view-doctor', views.patient_view_doctor_view,name='patient-view-doctor'),
    path('searchdoctor', views.search_doctor_view,name='searchdoctor'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),


    #cart
    path('product', views.ProductView, name='product'),
    path('order-summary', views.OrderSummaryView, name='order-summary'),
    path('add-to-cart/<pk>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', views.remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity-item/<pk>/', views.reduce_quantity_item, name='reduce-quantity-item')

    
]
   