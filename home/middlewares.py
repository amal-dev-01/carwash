from django.utils import timezone
from .models import Cart  # Replace with your actual model import

class DeleteExpiredModelInstancesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check and delete instances older than 5 minutes
        five_minutes_ago = timezone.now() - timezone.timedelta(minutes=5)
        expired=Cart.objects.filter(created_at__lte=five_minutes_ago)
        for i in expired:
            i.slot.is_available=True
            i.slot.save()
        expired.delete()
        response = self.get_response(request)
        return response
