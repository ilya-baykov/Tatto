from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
data_db = {
    "home": {"title": "Главная", "url_name": "home", "content_page": "Гланвая страница сайта"},
    "about": {"title": "О нас", "url_name": "about", "content_page": "Страница с информацией о нас"},
    "services": {"title": "Услуги", "url_name": "services", "content_page": "Страница с услугами"},
    "gallery": {"title": "Галерея", "url_name": "gallery", "content_page": "Галерея наших работ"},
    "sketches": {"title": "Эскизы", "url_name": "sketches", "content_page": "Тут будут скетчи"},
    "reviews": {"title": "Отзывы", "url_name": "reviews", "content_page": "Тут будут наши отзывы"},
    "prices": {"title": "Цены", "url_name": "prices", "content_page": "Тут будут цены"},
    "contacts": {"title": "Контакты", "url_name": "contacts", "content_page": "Тут будут наши контакты"},
}


def home_page(request):
    return render(request, 'tatto/home_page.html', context={"data_db": data_db})


def about_us_page(request):
    return render(request, 'tatto/about_us.html', context={"data_db": data_db})


def services_page(request):
    return render(request, 'tatto/services_page.html', context={"data_db": data_db})


def gallery_page(request):
    return render(request, 'tatto/gallery_page.html', context={"data_db": data_db})


def sketches_page(request):
    return render(request, 'tatto/sketches_page.html', context={"data_db": data_db})


def reviews_page(request):
    return render(request, 'tatto/reviews_page.html', context={"data_db": data_db})


def prices_page(request):
    return render(request, 'tatto/prices_page.html', context={"data_db": data_db})


def contacts_page(request):
    return render(request, 'tatto/contacts_page.html', context={"data_db": data_db})
