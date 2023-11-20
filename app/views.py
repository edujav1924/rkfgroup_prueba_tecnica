from django.core.cache import cache

import json
from django.views import View
import lzstring
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

class DownloadData(TemplateView):
    template_name = 'download_data.html'

    def get(self, request, *args, **kwargs):
        data = {
            'clientes': {
                '100': {
                    'nombrefantasia': 'Empresa_1 SA',
                    'nombrefactura': 'empresa_1',
                    'canalID': 1,
                    'ruc': '5552003-0'
                },
                '101': {
                    'nombrefantasia': 'Empresa_2 SA',
                    'nombrefactura': 'empresa_2',
                    'canalID': 2,
                    'ruc': '5552005-0'
                },
                '102': {
                    'nombrefantasia': 'Empresa_3 SA',
                    'nombrefactura': 'empresa_3',
                    'canalID': 3,
                    'ruc': '5552004-0'
                }
            },
            'articulos': {
                '9000': {
                    'descripcion': 'Laptop',
                    'precio': 1200,
                    'stock': 50
                },
                '9001': {
                    'descripcion': 'Teléfono',
                    'precio': 500,
                    'stock': 100
                },
                '9002': {
                    'descripcion': 'Radio',
                    'precio': 100,
                    'stock': 20
                },
            }
        }

        #Convertir a json la estructura.
        data_json = json.dumps(data)

        #Comprimir el json con lzstring.
        compressor = lzstring.LZString()

        #Guarda la estructura comprimida en la base de datos redis
        compressed = compressor.compressToUTF16(data_json)
        cache.set('data', compressed)
        data = cache.get('data')
        return super().get(request, *args, **kwargs)


class DonwloadApiView(View):

    def get(self, request, *args, **kwargs):
        # Your data to be serialized as JSON
        data = cache.get('data')
        data = {
            'message': data,
            'status': 'success'
        }

        # Create a JsonResponse object and return it
        return JsonResponse(data)
