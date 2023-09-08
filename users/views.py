from ast import Sub
import json
from django.http import JsonResponse, HttpRequest
from users.models import User, Subscriber
from campaigns.models import Campaign
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_subscriber(request: HttpRequest, campaign_id) -> JsonResponse:
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        first_name: str = data.get("first_name", '')
        email: str = data.get("email", '')

        if first_name and email:

            try:
                campaign = Campaign.objects.get(pk=campaign_id)
            except Campaign.DoesNotExist:
                return JsonResponse({'message': 'Campaign not found'}, status=404)
            try:
                user = User.objects.get(
                    email=email)
            except User.DoesNotExist:
                user = User.objects.create(first_name=first_name, email=email)

            is_subscribed = Subscriber.objects.filter(
                user=user, subscribed_campaigns=campaign)

            if is_subscribed:
                if is_subscribed[0].is_active:
                    return JsonResponse({'message': 'User is already subscribed to this campaign'})
                is_subscribed[0].is_active = True
                is_subscribed[0].save()
                return JsonResponse({'message': 'User subscribed to the campaign successfully',
                                    "data": {'first_name': first_name, "email": email, "campaign": campaign.subject}})

            sub = Subscriber.objects.create(
                user=user)

            sub.subscribed_campaigns.add(campaign)

            return JsonResponse({'message': 'User subscribed to the campaign successfully',
                                 "data": {'first_name': first_name, "email": email, "campaign": campaign.subject}})

        return JsonResponse({'message': 'Invalid data', "data": data}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
