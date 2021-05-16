import requests


def update_or_create_elements(response, update_create_element, obj):
    """
    Перебирает переданные в параметре элементы JSON'а и применяет к ним переденную в параметре функцию
    """
    for element in response.json():
        update_create_element(element, obj)
    return


def get_use_content(url, func, *args):
    """
    Запрашивает контент по определенному url и применяет к нему переданную в параметре функцию
    Возврает код ошибки HTTP запроса, если запрос неудачен.
    """
    response = requests.get(url=url)
    if response:
        return func(response, *args)
    else:
        print(f'Импорт данных завершился ошибкой: {response.status_code}.')
        return
