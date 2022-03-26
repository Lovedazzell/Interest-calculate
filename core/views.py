from pydoc import importfile
from django.shortcuts import render
from . forms import InterestCalForm
from. interest import find_interest

# Create your views here.
def dashboard(request):
    form = InterestCalForm()
    if request.method == 'POST':
        form = InterestCalForm(request.POST)
        if form.is_valid():
            uamount = int(form.cleaned_data['amount'])
            urelease = form.cleaned_data['release_date']
            total = find_interest(uamount,urelease)
            interest_amount = total-uamount
            context = {'grandtotal':int(total),'interest_rate':int(interest_amount)}
            return render(request,'result.html',context)
    context = {'form':form}
    return render(request,'index.html',context)