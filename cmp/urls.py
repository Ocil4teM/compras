from django.urls import path
from .views import ProveedorView, ProveedorNew, ProveedorEdit, proveedorInactivar,\
    ComprasView, compras

urlpatterns = [

    path('proveedor/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>', proveedorInactivar, name='proveedor_inactivar'),

    path('compras/', ComprasView.as_view(), name='compras_list'),
    path('compras/new',compras, name="compras_new"),
]