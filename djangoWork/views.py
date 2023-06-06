# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.contrib.auth import logout as auth_logout
from managerestaurants.models import Restaurants
from websiteservices.models import Feedback


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("hello sush")


def home(request):
    return render(request, 'index.html')
    # return HttpResponse("HOME")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("About Us")


def search(request):
    # allPosts = Restaurants.objects.all()
    query = request.GET['query']

    if len(query) > 10:
        allPosts = Restaurants.objects.none()
    else:
        allRestaurants = Restaurants.objects.filter(title__icontains=query)
        allRestaurantType = Restaurants.objects.filter(
            restaurantType__icontains=query)
        allPosts = allRestaurants.union(allRestaurantType)

    if allPosts.count() == 0:
        messages.error(request, "No search results found")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("Contact Us")


def handlelogin(request):
    if request.method == 'POST':
        logUserName = request.POST['logUserName']
        logPasswordField = request.POST['logPasswordField']

        user = authenticate(username=logUserName, password=logPasswordField)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')


def handlelogout(request):
    auth_logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')


def signup(request):
    # post parameters
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        emailField = request.POST['emailField']
        passwordField = request.POST['passwordField']

        if len(userName) < 6 or len(userName) > 30:
            messages.error(request, "Username contain at least 6 characters")
            return redirect('signup')

        # creating users
        myuser = User.objects.create_user(userName, emailField, passwordField)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')

    return render(request, 'signup.html')


def feedback(request):
    if request.method == 'POST':
        yourname = request.POST['yourname']
        youremail = request.POST['youremail']
        writefeedback = request.POST['writefeedback']

        fback = Feedback(customer_name=yourname,
                         email_address=youremail, suggestion=writefeedback)
        fback.save()
        messages.success(
            request, "Your feedback has been successfully submitted")
        return redirect('home')
    return render(request, 'feedback.html')


def restaurants(request):
    allposts = Restaurants.objects.all()
    context = {'allposts': allposts}
    return render(request, 'restaurants.html', context)


def EASTEASTASIANSPICETRAIL(request):
    return render(request, 'EAST-EAST_ASIAN_SPICE_TRAIL.html')


def THEEARTHPLATE(request):
    return render(request, 'THE_EARTH_PLATE.html')


def KEBABSANDKURRIES(request):
    return render(request, 'KEBABSANDKURRIES.html')


def NAMAK(request):
    return render(request, 'NAMAK.html')


def PESHAWRI(request):
    return render(request, 'PESHAWRI.html')


def other(request):
    return render(request, 'other.html')


def restaurant_analysis_1(request):
    return render(request, 'restaurant_analysis_1.html')


def restaurant_analysis_2(request):
    return render(request, 'restaurant_analysis_2.html')


def restaurant_analysis_3(request):
    return render(request, 'restaurant_analysis_3.html')


def restaurant_analysis_4(request):
    return render(request, 'restaurant_analysis_4.html')


def restaurant_analysis_5(request):
    return render(request, 'restaurant_analysis_5.html')
