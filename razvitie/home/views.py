from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Review
from .forms import ImageUploadForm
from django.http import JsonResponse

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    home_content = {'meta_description': "Кадровое агенство в Краснодаре",
                    'title_develop': "РАЗВИТИЕ | Кадровое агентство в Краснодаре",
                    'reviews': reviews,
                    }
    return render(request, 'home/index.html', context=home_content)


def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        if name and email and phone and subject and message:
            # sending email
            sended = send_mail(subject,  # subject
                               "ФИО: " + name + "\n\n" +
                               "Номер телефона: " + phone + "\n\n" + message,  # message review
                               email,  # from email
                               [settings.EMAIL_HOST_USER],  # to email
                               fail_silently=False)
            email_context = {
                'sended': sended,
            }
            return render(request, 'home/send.html', context=email_context)


def add_review(request):
    if request.method == 'POST':
        name = request.POST['name']
        qualify = request.POST['qualify']
        organization = request.POST['organization']
        body = request.POST['review']
       # image = ImageUploadForm(request.POST or None, request.FILES or None)
        if name and qualify and body \
                or organization and body \
                or name and qualify and organization and body \
                or name and organization and body:
            #print(name, qualify, organization, body)
            #print('name')
            # adding review to the database
            review = Review(name=name, qualification=qualify,
                            organization=organization, body=body)
            #if image.is_valid():
                #review.photo = image.cleaned_data['image']
            review.save()
            sended = False
            if review in Review.objects.all():
                sended = True
            review_context = {'sended': sended,}
            return render(request, 'home/review.html', context=review_context)


