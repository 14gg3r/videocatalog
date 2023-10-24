from django.urls import path

from .views import (add_video_catalog, export_to_excel, send_to_tg,
                    video_catalog_list)

urlpatterns = [
    # Другие URL-маршруты вашего приложения
    path('', video_catalog_list, name='video_catalog_list'),
    path('add/', add_video_catalog, name='add_video_catalog'),
    path('export_to_excel/', export_to_excel, name='export_to_excel'),
    path('send_to_tg/', send_to_tg, name='send_to_tg'),
]
