from django.shortcuts import render
from django.views import generic
from backend.models import MProductionWork, MCustomWork, MStoreInventory

'''
Notes:
Views for the accounting procedures are in the queries folder
'''

# Create your views here.
def pw(request):
    return render(request, 'pw.html', catalog)
    
def rm(request):
    return render(request, 'rm.html', catalog)

# Views to loop through for the catalog
class ProdoListView(generic.ListView):
    model = MProductionWork
    def get_context_data(self, **kwargs):
      context = super(ProdoListView, self).get_context_data(**kwargs)
      context['prodo'] = MProductionWork.objects.all()
      return context
                
class ProdoDetailView(generic.DetailView):
    model = MProductionWork
    def get_context_data(self, **kwargs):
      context = super(ProdoDetailView, self).get_context_data(**kwargs)
      context['prodo'] = MProductionWork.objects.all()
      return context

class CustomListView(generic.ListView):
    model = MCustomWork
        
class CustomDetailView(generic.DetailView):
    model = MCustomWork
    def get_context_data(self, **kwargs):
      context = super(CustomDetailView, self).get_context_data(**kwargs)
      context['custom'] = MCustomWork.objects.all()
      context['prodo'] = MProductionWork.objects.all()
      return context
        
class StoreInventoryListView(generic.ListView):
    model = MStoreInventory
    
class StoreInventoryDetailView(generic.DetailView):
    model = MStoreInventory
    def get_context_data(self, **kwargs):
      context = super(StoreInventoryDetailView, self).get_context_data(**kwargs)
      context['storeInventory'] = MStoreInventory.objects.all()
      context['prodo'] = MProductionWork.objects.all()
      return context


