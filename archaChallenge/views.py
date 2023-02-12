from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user, card

card1 = card.Card('1',"01/01/2024", 777, 10000.00,8000.00)
card2 = card.Card('2',"01/01/2024", 888, 10000.00,8000.00)
card3 = card.Card('3',"01/01/2024", 777, 10000.00,8000.00)
card4 = card.Card('4',"01/01/2024", 777, 10000.00,8000.00)
card5 = card.Card('5',"01/01/2024", 777, 10000.00,8000.00)
card6 = card.Card('6',"01/01/2024", 777, 10000.00,8000.00)

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html',{'name': 'Zhuoqing Zheng'})

def meView(request):
    user1 = user.User("zhuoqing", [1,2,3], "admin")
    user2 = user.User("Lewis Hamilton",[4,5,6],"user")
    thisUser = user1.__dict__

    secondUser = user2.__dict__
       
    allusers = {
        "currentuser" : thisUser,
        "otherusers" : [secondUser]
    }

   
    return render(request, 'me.html', allusers)


def cardView(request):

    data = { "cards" : [card1,card2,card3,card4,card5,card6],
            "level": "admin"}
    return render(request, "card.html" , data)
    
def changeLimit(request) :

    cards =  [card1,card2,card3,card4,card5,card6]

    for item in cards:
        if request.GET['cardNum1'] == item.cardNum:
          
            item.limit = float(request.POST['Limit'])
    

    
    data = { "cards" : [card1,card2,card3,card4,card5,card6],
            "level": "admin"}
    
    return redirect('/archa/card', "card.html" , data)
