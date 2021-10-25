from django.shortcuts import render, redirect
import random

def index(request):
    if 'curr_gold' not in request.session:
        request.session['curr_gold']=0 #this is where we're supposed to create this entry in the dictionary, right?
        request.session['stmt'] = []
    return render(request, "index.html")

# Create your views here.
def process_money(request):
    request.session['btn_press'] = request.POST['btn_press']
    print(request.session['btn_press'])
    if request.session['btn_press'] == "1":
        rand_gold_ct = random.randint(10,20)
        request.session['curr_gold']+=rand_gold_ct
        stmt = f"Earned {rand_gold_ct} gold from the farm!"
        request.session['stmt'].append(stmt)
    elif request.session['btn_press'] == "2":
        rand_gold_ct = random.randint(5,10)
        request.session['curr_gold']+=rand_gold_ct
        stmt = f"Earned {rand_gold_ct} gold from the cave!"
        request.session['stmt'].append(stmt)
    elif request.session['btn_press'] == "3":
        rand_gold_ct = random.randint(2,5)
        request.session['curr_gold']+=rand_gold_ct
        stmt = f"Earned {rand_gold_ct} gold from the house!"
        request.session['stmt'].append(stmt)
    elif request.session['btn_press'] == "4":
        rand_gold_ct = random.randint(-50,50)
        request.session['curr_gold']+=rand_gold_ct
        if rand_gold_ct >= 0:
            stmt = f"Earned {rand_gold_ct} gold from the casino!"
        else:
            stmt = f"Lost {rand_gold_ct} gold from the casino!"
        request.session['stmt'].append(stmt)
    return redirect("/") #not clear on precisely what needs to be returned here
