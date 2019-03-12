from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone

from products.models import Product


def home(request):
    return render(request, 'home.html')

@login_required(login_url='signup')
def create(request):
        if request.method=='POST':
            if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icons'] and request.FILES['image']:
                product = Product()
                product.title = request.POST['title']
                product.body = request.POST['body']

                if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                    product.url = request.POST['url']
                else:
                    product.url = 'http://'+request.POST['url']

                product.icons = request.FILES['icons']
                product.image = request.FILES['image']
                product.pub_date = timezone.datetime.now()
                product.hunter = request.user
                product.save()

                return redirect('/products/'+str(product.id))
            else:
                return render(request, 'create.html', {'error' : 'Please Enter all the required fields.'})

        else:

            return render(request,'create.html')



def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return  render(request,'details.html', {'product': product})


@login_required(login_url='signup')
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes += 1
        product.save()

        return redirect('/products/'+str(product.id))