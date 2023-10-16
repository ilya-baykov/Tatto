from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
data_db = [
    {"title": "Главная", "url_name": "home", "content": "Гланвая страница сайта"},
    {"title": "О нас", "url_name": "about", "content": "Страница с информацией о нас"},
    {"title": "Услуги", "url_name": "services", "content": "Страница с услугами"},
    {"title": "Галерея", "url_name": "gallery", "content": "Галерея наших работ"},
    {"title": "Эскизы", "url_name": "sketches", "content": "Тут будут скетчи"},
    {"title": "Отзывы", "url_name": "reviews", "content": "Тут будут наши отзывы"},
    {"title": "Цены", "url_name": "prices", "content": "Тут будут цены"},
    {"title": "Контакты", "url_name": "contacts", "content": "Тут будут наши контакты"},
]


def home_page(request):
    data = {
        "title": "Главная",
        "data_db": data_db
    }
    return render(request, 'tatto/home_page.html', context=data)


def about_us_page(request):
    data = {
        "title": "О нас",
        "data_db": data_db
    }
    return render(request, 'tatto/about_us.html', context=data)


def services_page(request):
    data = {
        "title": "Услуги",
        "data_db": data_db
    }
    return render(request, 'tatto/services_page.html', context=data)


def gallery_page(request):
    data = {
        "title": "Галерея",
        "data_db": data_db
    }
    return render(request, 'tatto/gallery_page.html', context=data)


def sketches_page(request):
    data = {
        "title": "Эскизы",
        "data_db": data_db
    }
    return render(request, 'tatto/sketches_page.html', context=data)


def reviews_page(request):
    data = {
        "title": "Отзывы",
        "data_db": data_db
    }
    return render(request, 'tatto/reviews_page.html', context=data)


def prices_page(request):
    data = {
        "title": "Цены",
        "data_db": data_db
    }
    return render(request, 'tatto/prices_page.html', context=data)


def contacts_page(request):
    data = {
        "title": "Контакты",
        "data_db": data_db
    }
    return render(request, 'tatto/contacts_page.html', context=data)
