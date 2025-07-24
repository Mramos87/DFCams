from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
# User registration view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Username and password required.')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('map')
    return render(request, 'cameras/register.html')

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('map')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'cameras/login.html')

# User logout view
def logout_view(request):
    logout(request)
    return redirect('map')
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
# User registration view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Username and password required.')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('map')
    return render(request, 'cameras/register.html')

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('map')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'cameras/login.html')

# User logout view
def logout_view(request):
    logout(request)
    return redirect('map')
from django.shortcuts import render



from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import CameraLocation
import json

def map_view(request):
    """
    Display a map with all camera locations.
    """
    return render(request, 'cameras/map.html')

def get_locations(request):
    """
    Return all APPROVED camera locations as JSON.
    """
    locations = list(CameraLocation.objects.filter(approved=True).values('id', 'description', 'latitude', 'longitude', 'created_at'))
    return JsonResponse({'locations': locations})

@csrf_exempt
def add_location(request):
    """
    Add a new camera location via POST (expects JSON: description, latitude, longitude).
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            description = data.get('description', '')
            latitude = float(data['latitude'])
            longitude = float(data['longitude'])
            loc = CameraLocation.objects.create(description=description, latitude=latitude, longitude=longitude, approved=False)
            return JsonResponse({'success': True, 'pending_moderation': True, 'message': 'Location submitted and pending moderator approval.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'POST required'}, status=405)
