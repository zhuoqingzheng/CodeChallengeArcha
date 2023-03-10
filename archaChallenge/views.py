from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user, card

# hard coded data, expected to be retrieved from database
user1 = user.User("zhuoqing", ['1','2'], "admin","archa")
user2 = user.User("Lewis Hamilton",['3','4'],"user","google")
user3 = user.User("Toto",['5'],"user","archa")
card1 = card.Card('1',"01/01/2024", 777, 10000.00,8000.00,user1)
card2 = card.Card('2',"01/01/2024", 888, 10000.00,8000.00,user1)
card3 = card.Card('3',"01/01/2024", 777, 10000.00,8000.00,user2)
card4 = card.Card('4',"01/01/2024", 777, 10000.00,8000.00,user2)
card5 = card.Card('5',"01/01/2024", 777, 10000.00,8000.00,user3)

cards =  [card1,card2,card3,card4,card5]


# first view created for test
def say_hello(request):
    return render(request, 'hello.html',{'name': 'Zhuoqing Zheng'})



# view for '/me' endpoint
def meView(request):

    thisUser = user1.__dict__

  

       
    allusers = {
        "currentuser" : thisUser,
        "otherusers" : [user2.__dict__,user3.__dict__]
    }

   
    return render(request, 'me.html', allusers)



# view for '/card' endpoint
def cardView(request):

    data = { "cards" : cards,
            "user": user1}
    return render(request, "card.html" , data)

# handles change limit operation    
def changeLimit(request) :

   
    #find the card and modify its limit
    for item in cards:
        if request.GET['cardNum1'] == item.cardNum:
            item.limit = float(request.POST['Limit'])
    

    
    data = { "cards" : cards,
            "user": "user1"}
    
    return redirect('/archa/card', "card.html" , data)
