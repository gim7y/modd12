class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # код, выполняемый до формирования ответа
        # (или другого middleware)

        response = self.get_response(request)

        # код, выполняемый после формирования запроса (или нижнего слоя)
        return response


# простой middleware, который отправляет пользователю соответ.версию
class MobileOrFullMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.mobile:
            prefix = "mobile/"
        else:
            prefix = "full/"
        response.template_name = prefix + response.template_name
        return response

