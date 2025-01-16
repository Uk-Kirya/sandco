import requests
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

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
        keywords = (
            "Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в Казахстане, производство "
            "песка, производство кварцпеска")

        description = "Крупнейшее производство фракционированного кварцевого песка в Казахстане"

        if request.method == "POST":
            return redirect("home")

        context = {
            'logos': Logos.objects.all(),
            'numbers': Number.objects.all(),
            'benefits': Benefit.objects.all(),
            'projects': Projects.objects.filter(is_published=True).order_by('date'),
            'news': News.objects.filter(is_published=True).order_by('date'),
            'spheres': Spheres.objects.all().order_by('order'),
            'lang': _('Hello World'),
            'keywords': keywords,
            'description': description,
        }
        return render(request, 'home.html', context=context)


class LibraryView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        keywords = (
            "Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в Казахстане, производство "
            "песка, производство кварцпеска")

        description = "Крупнейшее производство фракционированного кварцевого песка в Казахстане"

        context = {
            'products': Product.objects.filter(is_published=True).order_by('order'),
            'keywords': keywords,
            'description': description,
        }
        return render(request, 'library.html', context=context)


class LibraryDetailView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        category = get_object_or_404(Category, slug=slug)
        context = {
            'category': category,
            'advantages': Advantage.objects.filter(category=category).order_by('order'),
            'products': Product.objects.filter(is_published=True, category=category).order_by('order'),
            'projects': Projects.objects.filter(is_published=True, category=category).order_by('date'),
        }
        return render(request, 'library-details.html', context=context)


class CompanyView(TemplateView):
    template_name = 'company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keywords'] = ("Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в "
                               "Казахстане, производство песка, производство кварцпеска")

        context['description'] = ("Крупнейшее производство фракционированного кварцевого песка в Казахстане")

        return context


class OriginsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        keywords = (
            "Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в Казахстане, производство "
            "песка, производство кварцпеска")

        description = "Крупнейшее производство фракционированного кварцевого песка в Казахстане"

        context = {
            "history": History.objects.all(),
            "keywords": keywords,
            "description": description,
        }
        return render(request, 'origins.html', context=context)


class AboutProductView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        keywords = (
            "Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в Казахстане, производство "
            "песка, производство кварцпеска")

        description = "Крупнейшее производство фракционированного кварцевого песка в Казахстане"

        context = {
            "structure": Structure.objects.all(),
            "steps": Step.objects.all(),
            "keywords": keywords,
            "description": description,
            "products": Product.objects.filter(is_published=True).order_by('order'),
        }
        return render(request, 'about-product.html', context=context)


class ProjectsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        keywords = (
            "Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в Казахстане, производство "
            "песка, производство кварцпеска")

        description = "Крупнейшее производство фракционированного кварцевого песка в Казахстане"

        context = {
            "projects": Projects.objects.filter(is_published=True),
            "keywords": keywords,
            "description": description,

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
            'categories': Category.objects.all().filter(is_published=True).order_by('order'),
        }
        return render(request, 'project-details.html', context=context)


class TeamView(TemplateView):
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keywords'] = ("Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в "
                               "Казахстане, производство песка, производство кварцпеска")

        context['description'] = ("Крупнейшее производство фракционированного кварцевого песка в Казахстане")

        return context


class NewsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        keywords = (
            "Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в Казахстане, производство "
            "песка, производство кварцпеска")

        description = "Крупнейшее производство фракционированного кварцевого песка в Казахстане"

        news = News.objects.filter(is_published=True)
        context = {
            "news": news,
            "keywords": keywords,
            "description": description,
        }
        return render(request, 'news.html', context=context)


class NewsDetailsView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        new = get_object_or_404(News, slug=slug)
        news = News.objects.filter(is_published=True)
        context = {
            "new": new,
            "news": news,
        }
        return render(request, 'news-details.html', context=context)


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keywords'] = ("Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в "
                               "Казахстане, производство песка, производство кварцпеска")

        context['description'] = ("Крупнейшее производство фракционированного кварцевого песка в Казахстане")

        return context


class PolicyView(TemplateView):
    template_name = 'policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keywords'] = ("Фракционированный песок, кварцпесок, песок, песок в Казахстане, кварцпесок в "
                               "Казахстане, производство песка, производство кварцпеска")

        context['description'] = ("Крупнейшее производство фракционированного кварцевого песка в Казахстане")

        return context


class ProductDetailsView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        product = get_object_or_404(Product, slug=slug)
        context = {
            'product': product,
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
        category = request.POST.get('category', 'Онлайн заявка')
        value = request.POST.get('value', '—')
        package = request.POST.get('package', '—')
        deadlines = request.POST.get('deadlines', '—')
        recaptcha_response = request.POST.get('g-recaptcha-response')

        data = {
            'secret': '6Lf4Aw0qAAAAAINI-ifpdqfbog9EhA4IiRyNO8Ur',
            'response': recaptcha_response
        }

        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if not result['success']:
            return HttpResponse('Ошибка заполнения reCaptcha', status=400)

        new_application = Application(
            name=name,
            phone=phone,
            email=email,
            category=category,
            value=value,
            package=package,
            deadlines=deadlines
        )
        new_application.save()

        # Отправляем заявку на почту
        subject = 'Онлайн заявка с сайта Sandco.kz'
        message = (f'Имя: {name}\n'
                   f'Телефон: {phone}\n'
                   f'Email: {email}\n'
                   f'Интересующее направление: {category}\n'
                   f'Объем (м3): {value}\n'
                   f'Упаковка: {package}\n'
                   f'Сроки поставки: {deadlines}')
        from_email = 'udarnik.kirill@mail.ru'
        recipient_list = ['sand@sandco.kz']
        send_mail(subject, message, from_email, recipient_list)

        # Отправляем заявку в Arcuda
        url_arcude = "https://demo.arcuda.kz/sp/sandco"
        headers_arcude = {
            "Content-Type": "application/json",
            "Authorization": "Basic c3BTYW5kY286aGRRS3J0WkAyMw==",
        }
        data_arcude = {
            "name": name,
            "phone": phone,
            "email": email,
            "category": category,
            "value": value,
            "package": package,
            "deadlines": deadlines,
        }
        requests.post(url_arcude, headers=headers_arcude, data=json.dumps(data_arcude))

        url = reverse("catalog:application_success")
        return redirect(url)


class ProductApplicationView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        product = request.POST.get('product')
        category = request.POST.get('category')
        value = request.POST.get('value')
        package = request.POST.get('package')
        deadlines = request.POST.get('deadlines')
        recaptcha_response = request.POST.get('g-recaptcha-response')

        data = {
            'secret': '6Lf4Aw0qAAAAAINI-ifpdqfbog9EhA4IiRyNO8Ur',
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if not result['success']:
            return HttpResponse('Ошибка заполнения reCaptcha', status=400)

        new_product_application = ProductApplication(name=name, phone=phone, email=email, product=product, category=category, value=value, package=package, deadlines=deadlines)
        new_product_application.save()

        # Отправляем заявку на почту
        subject = 'Заказ товара с сайта Sandco.kz'
        message = f'Имя: {name}\nТелефон: {phone}\nEmail: {email}\nТовар: {product},\nИнтересующее направление: {category}\nОбъем (м3): {value}\nУпаковка: {package}\nСроки поставки: {deadlines}'
        from_email = 'udarnik.kirill@mail.ru'
        recipient_list = ['sand@sandco.kz']
        send_mail(subject, message, from_email, recipient_list)

        # Отправляем заявку в Arcuda
        url_arcude = "https://demo.arcuda.kz/sp/sandco"
        headers_arcude = {
            "Content-Type": "application/json",
            "Authorization": "Basic c3BTYW5kY286aGRRS3J0WkAyMw==",
        }
        data_arcude = {
            "name": name,
            "phone": phone,
            "email": email,
            "category": category,
            "value": value,
            "package": package,
            "deadlines": deadlines,
        }
        requests.post(url_arcude, headers=headers_arcude, data=json.dumps(data_arcude))

        url = reverse("catalog:application_success")
        return redirect(url)


class ApplicationSuccessView(View):
    template_name = 'send-application.html'

    def get(self, request):
        return render(request, self.template_name)
