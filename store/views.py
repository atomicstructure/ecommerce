from django.shortcuts import get_object_or_404, render
from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from store.models import Products
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Products.objects.all().filter(is_available=True).order_by('id')
        # Pagination
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
     
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    colors = single_product.color.split(',')
    sizes = single_product.size.split(',')
    product_reviews = single_product.reviews.all()
    product_gallery = single_product.product_gallery.all()
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'colors': colors,
        'sizes': sizes,
        'product_reviews': product_reviews,
        'product_gallery': product_gallery
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    products = Products.objects.all().filter(is_available=True)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Products.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)
