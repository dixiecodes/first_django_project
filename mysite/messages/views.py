from django.http import JsonResponse

# Create your views here.

data = {
"Name" : "Dixie Sasu",
"Track" : "Backend (Python)",
"Message" : "Hi, mentors, thank you for this experience!"
}


def data_index(request):
    return JsonResponse(data)