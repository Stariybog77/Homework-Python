#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import requests

# =========================
# ДЕКОРАТОР (ограничение вызова)
# =========================
def rate_limit(seconds):
    def decorator(func):
        last_time = [0]

        def wrapper(*args, **kwargs):
            current_time = time.time()

            if current_time - last_time[0] < seconds:
                print("Слишком частый вызов функции!")
                return None

            last_time[0] = current_time
            return func(*args, **kwargs)

        return wrapper
    return decorator


# =========================
# ЗАМЫКАНИЕ (API запрос)
# =========================
def get_dog_fact():
    url = "https://dogapi.dog/api/v2/facts"

    def fetch():
        try:
            response = requests.get(url)
            data = response.json()
            return data["data"][0]["attributes"]["body"]
        except Exception as e:
            return f"Ошибка: {e}"

    return fetch


# =========================
# ПРИМЕНЕНИЕ ДЕКОРАТОРА
# =========================
@rate_limit(5)  # можно вызывать раз в 5 секунд
def get_fact():
    fetch = get_dog_fact()
    return fetch()


# =========================
# ЗАПУСК
# =========================
if __name__ == "__main__":
    print("Факт 1:", get_fact())

    print("Пробуем вызвать сразу ещё раз:")
    print("Факт 2:", get_fact())

    print("Ждём 5 секунд...")
    time.sleep(5)

    print("Факт 3:", get_fact())