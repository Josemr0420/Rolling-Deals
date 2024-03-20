from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HotwheelForm, AuctionForm, BidForm
from .models import Auction, Hotwheel
from django.shortcuts import get_object_or_404, render

def search_auctions(request):
    queryset = Auction.objects.select_related('hotwheel').all()
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')
    color = request.GET.get('color')

    if min_year and max_year:
        queryset = queryset.filter(hotwheel__year_released__range=(min_year, max_year))
    if color:
        queryset = queryset.filter(hotwheel__color__icontains=color)

    return render(request, 'auction/search.html', {'auctions': queryset})



@login_required
def create_auction(request):
    if request.method == 'POST':
        auction_form = AuctionForm(request.POST)
        hotwheel_form = HotwheelForm(request.POST, request.FILES)

        if 'hotwheel' in request.POST and request.POST['hotwheel']:
            if auction_form.is_valid():
                auction = auction_form.save(commit=False)
                auction.user = request.user
                auction.hotwheel_id = request.POST['hotwheel']
                auction.save()
                return redirect('auction')
        else:
            if hotwheel_form.is_valid() and auction_form.is_valid():
                hotwheel = hotwheel_form.save()
                auction = auction_form.save(commit=False)
                auction.hotwheel = hotwheel
                auction.user = request.user
                auction.save()
                return redirect('auction')
            else:
                # Si hay errores, muestra el formulario nuevamente
                return render(request, 'auction/create_auction.html', {
                    'auction_form': auction_form,
                    'hotwheel_form': hotwheel_form
                })

    else:
        auction_form = AuctionForm()
        hotwheel_form = HotwheelForm()

    return render(request, 'auction/create_auction.html', {
        'auction_form': auction_form,
        'hotwheel_form': hotwheel_form
    })

def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    highest_bid = auction.bids.order_by('-amount').first()
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.auction = auction
            # Asegúrate de validar si la puja es mayor que la puja actual más alta
            highest_bid = auction.bids.order_by('-amount').first()
            if not highest_bid or bid.amount > highest_bid.amount:
                bid.save()
                messages.success(request, "Tu puja ha sido exitosa.")
                return redirect('auction_detail', auction_id=auction.id)
            else:
                messages.error(request, "Tu puja debe ser mayor que la puja actual más alta.")
    else:
        form = BidForm()

    return render(request, 'auction/auction_detail.html', {
        'auction': auction,
        'form': form,
        'highest_bid': highest_bid
    })


