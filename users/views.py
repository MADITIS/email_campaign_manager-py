from django.http import JsonResponse, HttpRequest
from users.models import User


def add_subscriber(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        first_name: str = request.POST.get("first_name", '')
        email: str = request.POST.get("email", '')

        if email and first_name:
            subscriber, created = User.objects.get_or_create(email=email)
            if created:
                subscriber.first_name = first_name
                subscriber.save()
                return JsonResponse({'message': 'Subscriber added successfully'})
            else:
                return JsonResponse({'message': 'Subscriber with this email already exists'})
        else:
            return JsonResponse({'message': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
