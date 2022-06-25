from django.shortcuts import render, redirect, reverse, HttpResponse

# Created views 

def view_bag(request):
    """ View that renders the bag page contents """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add qty of product to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
             
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

    

def adjust_bag(request, item_id):
    """ Adjust qty of different products in shopping bag """

    quantity = int(request.POST.get('quantity'))
     
     
    if quantity > 0:
            bag[item_id] = quantity
    else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

 
def remove_bag(request, item_id):
    """ Adjust qty of different products in shopping bag """

    try:
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
