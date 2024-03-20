from django import forms
from .models import Hotwheel, Auction, Bid


class HotwheelForm(forms.ModelForm):

    class Meta:
        model = Hotwheel
        fields = ['model_name', 'year_released', 'color', 'image']


class AuctionForm(forms.ModelForm):
    hotwheel = forms.ModelChoiceField(queryset=Hotwheel.objects.all(), required=False, empty_label="None")

    class Meta:
        model = Auction
        fields = ['start_time', 'end_time', 'starting_bid', 'status']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
