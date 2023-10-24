import requests
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from openpyxl import Workbook

from .forms import VideoCatalogForm
from .models import VideoCatalog


def video_catalog_list(request):
    video_catalogs = VideoCatalog.objects.all()
    return render(request, 'video_catalog_list.html', {'video_catalogs': video_catalogs})


def add_video_catalog(request):
    if request.method == 'POST':
        form = VideoCatalogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись добавлена")
            return redirect('add_video_catalog')
        else:
            messages.error(request, "Ошибка в форме")
    else:
        form = VideoCatalogForm()

    return render(request, 'add_video_catalog.html', {'form': form})


def export_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="video_catalog.xlsx"'
    wb = Workbook()
    ws = wb.active
    headers = ['№ каталога', 'Исполнитель', 'Название', 'Хронометраж', 'Тип', 'Режиссёр', 'Сценарист', 'Композитор',
               'Год', 'Youtube', 'RuTube', 'Яндекс', 'VK', 'Дзен', 'UPC']
    ws.append(headers)
    data = VideoCatalog.objects.all()

    for item in data:
        row = [item.catalog_number, item.performer, item.title, item.duration, item.video_type, item.director,
               item.screenwriter, item.composer, item.year, item.youtube_link, item.rutube_link, item.yandex_link,
               item.vk_link, item.zen_link,
               item.upc]
        ws.append(row)

    wb.save(response)

    return response


def send_to_tg(request):
    data = VideoCatalog.objects.all()
    for item in data:
        message = ''
        message += f'№ каталога: {item.catalog_number}\n'
        message += f'Исполнитель: {item.performer}\n'
        message += f'Название: {item.title}\n'
        message += f'Хронометраж: {item.duration}\n'
        message += f'Тип: {item.video_type}\n'
        message += f'Режиссёр: {item.director}\n'
        message += f'Сценарист: {item.screenwriter}\n'
        message += f'Композитор: {item.composer}\n'
        message += f'Год: {item.year}\n'
        message += 'Youtue: ' + f'[Ссылка]({item.youtube_link})' if item.youtube_link else 'Youtue: -'
        message += '\nRuTube: ' + f'[Ссылка]({item.rutube_link})' if item.rutube_link else '\nRuTube: -'
        message += '\nЯндекс: ' + f'[Ссылка]({item.yandex_link})' if item.yandex_link else '\nЯндекс: -'
        message += '\nVK: ' + f'[Ссылка]({item.vk_link})' if item.vk_link else '\nVK: -'
        message += '\nДзен: ' + f'[Ссылка]({item.zen_link})' if item.zen_link else '\nДзен: -'
        message += f'\nUPC: {item.upc}\n\n'
        if item.files:
            params = {
                'chat_id': settings.TELEGRAM_CHAT_ID,
                'caption': message,
                'parse_mode': 'markdown',
            }
            with open(item.files.path, 'rb') as file:
                files = {'document': (item.files.name, file)}
                response = requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/sendDocument',
                                        params=params, files=files)
        else:
            params = {
                'chat_id': settings.TELEGRAM_CHAT_ID,
                'text': message,
                'parse_mode': 'markdown'
            }
            response = requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/sendMessage',
                                    params=params)
        if response.status_code == 200:
            messages.success(request, "Данные отправлены в телеграм")
            print('Сообщение успешно отправлено')
        else:
            messages.error(request, "Ошибка при отправке сообщения:" + response.text)
            print('Ошибка при отправке сообщения:', response.text)
    return redirect('video_catalog_list')
