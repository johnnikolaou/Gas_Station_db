from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consists_of/', views.consistsOf, name='consistsOf'),
    path('consists_of/<str:supply_prod>/', views.consistsOf_delete),
    path('contract/', views.contract, name='contract'),
    path('contract/<int:id>/', views.contract_delete),
    path('customer/', views.customer, name='customer'),
    path('customer/<str:email>/', views.customer_delete),
    path('employee/', views.employee, name='employee'),
    path('employee/<str:ssn>/', views.employee_delete),
    path('entails/', views.entails, name='entails'),
    path('entails/<str:serv_pur>/', views.entails_delete),
    path('gas_stations/', views.gasStation, name='gasStation'),
    path('gas_stations/<str:longitude_latitude>/', views.gasStation_delete),
    path('involves/', views.involves, name='involves'),
    path('involves/<str:prod_pur>/', views.involves_delete),
    path('is_assigned_to/', views.isAssignedTo, name='isAssignedTo'),
    path('offers/', views.offers, name='offers'),
    path('product/', views.product, name='product'),
    path('product/<int:id>/', views.product_delete),
    path('provides/', views.provides, name='provides'),
    path('provides/<str:serv_gslong_lat>/', views.provides_delete),
    path('pumps/', views.pump, name='pump'),
    path('purchases/', views.purchase, name='purchase'),
    path('service/', views.service, name='service'),
    path('service/<int:id>/', views.service_delete),
    path('signs/', views.sign, name='sign'),
    path('signs/<str:essn_contract>/', views.sign_delete),
    path('supplier/', views.supplier, name='supplier'),
    path('supplier/<str:email>/', views.supplier_delete),
    path('supply/', views.supply, name='supply'),
    path('supply/<int:id>/', views.supply_delete),
    path('tanks/', views.tank, name='tank'),
    path('tanks/<str:id_longitude_latitude>/', views.tank_delete)
]