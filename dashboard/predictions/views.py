from django.shortcuts import render
from .models import CustomerPredictions

def dashboard(request):
    total = CustomerPredictions.objects.count()
    predicted_buy = CustomerPredictions.objects.filter(prediction=1).count()
    predicted_not_buy = CustomerPredictions.objects.filter(prediction=0).count()
    actual_buy = CustomerPredictions.objects.filter(will_purchase=1).count()
    actual_not_buy = CustomerPredictions.objects.filter(will_purchase=0).count()

    context = {
        'total': total,
        'predicted_buy': predicted_buy,
        'predicted_not_buy': predicted_not_buy,
        'actual_buy': actual_buy,
        'actual_not_buy': actual_not_buy,
        'accuracy': round((predicted_buy + predicted_not_buy) / total * 100, 2) if total > 0 else 0,
    }
    return render(request, 'predictions/dashboard.html', context)