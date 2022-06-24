from django.urls import path, include
from backend.queries import views as qv
from backend import views
from django.conf import settings
from django.conf.urls.static import static

'''
Notes:
Notice the qv is the views from queries and the views are the accounting directory
'''

urlpatterns = [
    path('inventory/', qv.inventory, name='inventory'),
    path('pw/', views.pw, name='pw'),
    path('rm/', views.rm, name='rm'),
    path('assets/', qv.assets, name='assets'),
    path('ff/', qv.furniturefixtures, name='ff'),
    path('liabilities/', qv.liabilities, name='liabilities'),
    path('revexpoe/', qv.revexpoe, name='revexpoe'),
    path('reports/', qv.reports, name='reports'),
    path('prodo/', views.ProdoListView.as_view(), name='prodo'),
    path('prodo/<int:pk>', views.ProdoDetailView.as_view(), name='prodo-detail'),
    path('custom/', views.CustomListView.as_view(), name='custom'),
    path('custom/<int:pk>', views.CustomDetailView.as_view(), name='custom-detail'),
    path('storeInventory/', views.StoreInventoryListView.as_view(), name='storeInventory'),
    path('storeInventory/<int:pk>', views.StoreInventoryDetailView.as_view(), name='storeInventory-detail'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)