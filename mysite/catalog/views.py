import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.core.mail import send_mail

from .models import (
    Logos,
    Number,
    Benefit,
    Structure,
    Step,
    History,
    News,
    Projects,
    ProjectPhoto,
    Category,
    Advantage,
    Product,
    ProductPhoto,
    Spheres,
    Application,
    ProductApplication,
)


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.method == "POST":
            return redirect("home")

        context = {
            'logos': Logos.objects.all(),
            'numbers': Number.objects.all(),
            'benefits': Benefit.objects.all(),
            'projects': Projects.objects.filter(is_published=True).order_by('date'),
            'news': News.objects.filter(is_published=True).order_by('date'),
            'spheres': Spheres.objects.all().order_by('order'),
        }
        return render(request, 'home.html', context=context)


class LibraryView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'categories': Category.objects.filter(is_published=True).order_by('order'),
            'products': Product.objects.filter(is_published=True).order_by('order'),
        }
        return render(request, 'library.html', context=context)


class LibraryDetailView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        category = get_object_or_404(Category, slug=slug)
        context = {
            'category': category,
            'categories': Category.objects.filter(is_published=True).order_by('order'),
            'advantages': Advantage.objects.filter(category=category).order_by('order'),
            'products': Product.objects.filter(is_published=True, category=category).order_by('order'),
            'projects': Projects.objects.filter(is_published=True, category=category).order_by('date'),
        }
        return render(request, 'library-details.html', context=context)


class CompanyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'company.html')


class OriginsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "history": History.objects.all(),
        }
        return render(request, 'origins.html', context=context)


class AboutProductView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "structure": Structure.objects.all(),
            "steps": Step.objects.all(),
            "products": Product.objects.filter(is_published=True).order_by('order'),
        }
        return render(request, 'about-product.html', context=context)


class ProjectsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "projects": Projects.objects.filter(is_published=True),
        }
        return render(request, 'projects.html', context=context)


class ProjectDetailView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        project = get_object_or_404(Projects, slug=slug)
        context = {
            "project": project,
            "projects": Projects.objects.filter(is_published=True),
            "photos": ProjectPhoto.objects.filter(project=project),
            "products": Product.objects.filter(is_published=True, products_projects=project).order_by('order'),
        }
        return render(request, 'project-details.html', context=context)


class TeamView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'team.html')


class NewsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "news": News.objects.filter(is_published=True),
        }
        return render(request, 'news.html', context=context)


class NewsDetailsView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        new = get_object_or_404(News, slug=slug)
        context = {
            "new": new,
            "news": News.objects.filter(is_published=True),
        }
        return render(request, 'news-details.html', context=context)


class ContactsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'contacts.html')


class PolicyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'policy.html')


class ProductDetailsView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        product = get_object_or_404(Product, slug=slug)
        context = {
            'product': product,
            'categories': Category.objects.filter(is_published=True, products=product).order_by('order'),
            'library': Category.objects.filter(is_published=True).order_by('order'),
            'photos': ProductPhoto.objects.filter(product=product),
            'projects': Projects.objects.filter(is_published=True, product=product).order_by('date'),
        }
        return render(request, 'product-details.html', context=context)


class SendApplication(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        recaptcha_response = request.POST.get('g-recaptcha-response')

        data = {
            'secret': '6Lf4Aw0qAAAAAINI-ifpdqfbog9EhA4IiRyNO8Ur',
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if not result['success']:
            return HttpResponse('Ошибка заполнения reCaptcha', status=400)

        new_application = Application(name=name, phone=phone, email=email)
        new_application.save()

        # Отправляем заявку на почту
        subject = 'Онлайн заявка с сайта Sandco.kz'
        message = f'Имя: {name}\nТелефон: {phone}\nEmail: {email}'
        from_email = 'udarnik.kirill@mail.ru'
        recipient_list = ['sand@sandco.kz']
        send_mail(subject, message, from_email, recipient_list)

        url = reverse("catalog:application_success")
        return redirect(url)


class ProductApplicationView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        product = request.POST.get('product')
        recaptcha_response = request.POST.get('g-recaptcha-response')

        data = {
            'secret': '6Lf4Aw0qAAAAAINI-ifpdqfbog9EhA4IiRyNO8Ur',
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if not result['success']:
            return HttpResponse('Ошибка заполнения reCaptcha', status=400)

        new_product_application = ProductApplication(name=name, phone=phone, email=email, product=product)
        new_product_application.save()

        # Отправляем заявку на почту
        subject = 'Заказ товара с сайта Sandco.kz'
        message = f'Имя: {name}\nТелефон: {phone}\nEmail: {email}\nТовар: {product}'
        from_email = 'udarnik.kirill@mail.ru'
        recipient_list = ['sand@sandco.kz']
        send_mail(subject, message, from_email, recipient_list)

        url = reverse("catalog:application_success")
        return redirect(url)


class ApplicationSuccessView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'send-application.html')
