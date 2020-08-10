from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from django.core.mail import EmailMessage
from validate_email import validate_email
from django.template.loader import render_to_string
from django.views import View
from .utils import token_generator

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

import threading


class EmailThread(threading.Thread):
    def __init__(self, email_message):
        self.email_message=email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send()


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if username == "" or first_name == "" or password1 == "" or password2 == "" or email == "":
            messages.info(request, 'Необходимо заполнить все поля!')
            return redirect('register')
        if "@" not in email or "." not in email:
            messages.info(request, 'Почта введена неправильно')
            return redirect('register')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Данное имя пользователя занято')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Данная электронная почта уже зарегистрирована')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name)
                user.is_active = False
                user.save()

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})
                activate_url = 'http://' + domain + link
                email_subject = 'Активация аккаунта'
                email_body = 'Здравствуйте ' + user.username + '! Для активации вашего аккаунта перейдите ' \
                                                                  'по ссылке для подтверждения вашей ' \
                                                                  'электронной почты:\n' + activate_url
                email_message = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],
                )

                EmailThread(email_message).start()

                messages.success(request, 'Ссылка для активации аккаунта отправлена на вашу электронную почту')
        else:
            messages.info(request, 'Пароли не совпадают')
            return redirect('register')
        return redirect('register')
    else:
        return render(request, 'english/register.html')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('login' + '?message' + 'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Аккаунт успешно активирован')
            return redirect('login')
        except:
            pass

        return redirect('login')


class RequestResetEmailView(View):
    def get(self, request):
        return render(request, 'english/request-reset-email.html')


    def post(self, request):
        email = request.POST['email']

        if not validate_email(email):
            messages.info(request, 'Введена неправильная электронная почта')
            return render(request, 'english/request-reset-email.html')

        user = User.objects.filter(email=email)

        if user.exists():
            current_site = get_current_site(request)
            email_subject = 'Смена пароля'
            message = render_to_string('english/reset-user-password.html',
                                        {
                                            'domain': current_site.domain,
                                            'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                                            'token': PasswordResetTokenGenerator().make_token(user[0])
                                        }
                                        )
            email_message = EmailMessage(
                email_subject,
                message,
                'noreply@semycolon.com',
                [email]
            )

            EmailThread(email_message).start()

            messages.success(request, 'Вам отправлено письмо с инструкцией')
            return render(request, 'english/request-reset-email.html')
        else:
            messages.info(request, 'Введена неправильная электронная почта')
            return render(request, 'english/request-reset-email.html')


class SetNewPasswordView(View):
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }
        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.info(request, 'Данная ссылка уже была использована, отправьте новый запрос')
                return render(request, 'english/request-reset-email.html')

        except DjangoUnicodeDecodeError as identifier:
            messages.info(request, 'Данная ссылка уже была использована, отправьте новый запрос')
            return render(request, 'english/request-reset-email.html')

        return render(request, 'english/set-new-password.html', context)

    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
            'has_error': False
        }
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if len(password) < 6:
            messages.add_message(request, messages.ERROR, 'Слишком короткий пароль')
            context['has_error'] = True
            return render(request, 'english/set-new-password.html', context)

        if password != password2:
            messages.add_message(request, messages.ERROR, 'Пароли не совпадают')
            context['has_error'] = True
            return render(request, 'english/set-new-password.html', context)

        if context['has_error'] == True:
            return render(request, 'english/set-new-password.html', context)

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()

            messages.success(request, 'Вы успешно изменили пароль')
            return redirect('login')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, 'Что-то пошло не так!')
            return render(request, 'english/set-new-password.html', context)

        return render(request, 'english/set-new-password.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Введены неправильные данные")
            return redirect("login")
    else:
        return render(request, 'english/login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
