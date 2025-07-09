from django.shortcuts import render
from django.http import HttpResponse

Info =[
    {
        'Name':'Zhou Mingrui / Klien Moretti',
        'Title':'The Fool/The World',
        'Status':'Fused/Slumber',
        'Sequence':'Lord of The Mysteries',
        'Predecessor':'Celestial Worthy'
    },
    {
        'Name':'Adam',
        'Title':'The Spectator',
        'Status':'Dead',
        'Sequence':'God Almighty',
        'Predecessor':'Promodial God Almighty'

    }
]

def home(request):
    bio = {
        'Information' :Info
    }
    return render(request,'blog/home.html',bio)

def about(request):
    return render(request,'blog/about.html',{'Sequence':'Great Old One'})

