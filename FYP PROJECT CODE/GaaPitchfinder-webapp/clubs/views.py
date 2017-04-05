from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post , Club
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# if the user is logged in they can use this funtionality where they can post information
# not implemented visually
@login_required
def create(request):
    if request.method =='POST':
        if request.POST['title'] and request.POST['url']:
            post = models.Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return render(request, 'clubs/home.html')
        else:
            return render(request, 'clubs/create.html', {'error':'Sorry, You need to have both a title and a Url to create a post.'})

    else:
        return render(request, 'clubs/create.html')

# brings the user to the home page 
def home(request):
    # if query has a value, delete it so that it can be set to null for the next query
    try:
        del request.session['query']
    except: 
        query = ""
        
    # send user to home page
    return render(request, 'clubs/home.html')
    
# lists the counties based on the selection of county on the home screen 
def listingCounties(request):
    try:
        # if the method is POST set query to recieve the input and set it as a session variable
        if request.method =='POST':
            
            query = ""            
            query = request.POST.get('County', "")
            request.session['query'] = query
            # filters the club by the selected county in "query"
            clubs_list = Club.objects.filter(county__icontains= request.session['query'])
            
        else:
            # filters the club by the selected county already in "query"
            clubs_list = Club.objects.filter(county__icontains= request.session['query'])
            
    except KeyError:
        
        #if theres an error revery back to the query being a name of a club like in "listing"
        query = ""
        clubs_list = Club.objects.order_by('name')

    # shows a max of 15 clubs then overflows onto the next page
    paginator = Paginator(clubs_list, 15)
    page = request.GET.get('page')
    
    try:
        
        # sorts the clubs into pages and shows the number at bottom of screen
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(1)
        
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(paginator.num_pages)
        
    except query:
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page()

    # sends user to county.html
    return render(request, 'clubs/county.html', {'clubs':clubs})
    

    
# lists the counties based on the search of club name on the home screen 
def listing(request):
    try:
        # if the method is POST set query to recieve the input and set it as a session variable
        if request.method =='POST':
            
            query = request.POST.get('search_clubs', "")
            request.session['query'] = query
            clubs_list = Club.objects.filter(name__icontains= request.session['query'])
            
        else:
            # filters the club by the selected county already in "query"
            clubs_list = Club.objects.filter(name__icontains= request.session['query'])
            
    except KeyError:
        
        #if theres an error revery back to the query being a name of a club
        query = ""
        clubs_list = Club.objects.order_by('name')

    # shows a max of 15 clubs then overflows onto the next page
    paginator = Paginator(clubs_list, 15)
    page = request.GET.get('page')
    
    try:
        
        # sorts the clubs into pages and shows the number at bottom of screen
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(1)
        
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page(paginator.num_pages)
        
    except query:
        
        clubs = paginator.object_list.order_by('name')
        clubs = paginator.page()

    # sends user to club.html
    return render(request, 'clubs/club.html', {'clubs':clubs})
    

