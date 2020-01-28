from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [
            {
            "restaurant_name" : "Johnny Rockets",
            "food_type" : "Burgers and Fries",
        },
        {
            "restaurant_name" : "Tatami",
            "food_type" : "Sushi",
        },
        {
            "restaurant_name" : "Pick",
            "food_type" : "Yogurt",
        },
        ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": 
            {
            "restaurant_name" : "Pick",
            "food_type" : "Yogurt",
        }

    }
    return render(request, 'detail.html', context)
