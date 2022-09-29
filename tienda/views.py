from django.shortcuts import render,get_object_or_404
from.models import Producto
from.models import Categoria
# Create your views here.
def index(request):
    product_list=Producto.objects.all()
    product_cate=Categoria.objects.all()
    context={
        'product_list':product_list,
        'product_cate':product_cate
        }
    return render(request,'index.html',context)
    

def producto(request,producto_id):
    producto=get_object_or_404(Producto,pk=producto_id)
    cate=Categoria.objects.all()
    
    return render(request,'producto.html', {'producto':producto,'cate':cate})
