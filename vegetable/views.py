from django.shortcuts import render, redirect
from .models import Receipe
# Create your views here.
def home(request):
    return render(request, 'vegetable/index.html')

def receipe(request):
    if request.method=='POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe = Receipe(receipe_name=receipe_name, receipe_description=receipe_description, receipe_image=receipe_image)
        receipe.save()
        print(receipe_image)
        # print(data.receipe_name)
    return render(request,'vegetable/receipe.html')

def viewReceipe(request):
    receipes = Receipe.objects.all()
    return render(request,'vegetable/receipeDetails.html',{'receipes':receipes})

def deleteReceipe(request, id):
   delete_query = Receipe.objects.get(id=id)
   delete_query.delete()
   return redirect('view-receipe')


def updateReceipe(request, id):
    update_query = Receipe.objects.get(id=id)
    context = {'receipe':update_query}
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        update_query.receipe_name=receipe_name
        update_query.receipe_description=receipe_description
        update_query.save()
        return redirect('view-receipe')
    return render(request,'vegetable/updateReceipe.html',context)