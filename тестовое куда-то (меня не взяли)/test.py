import requests
import json

base_url = "https://4lapy.ru/api/goods_list_cached/"
headers = {
    "Host": "4lapy.ru",
    "Cookie": "selected_city_code=0000073738",
    "User-Agent": "v4.1.4(Android 7.1.2, samsung SM-G988N)",
    "Version-Build": "184",
    "Authorization": "Basic NGxhcHltb2JpbGU6eEo5dzFRMyhy",
    "X-Apps-Build": "4.1.4(184)",
    "X-Apps-Os": "7.1.2",
    "X-Apps-Screen": "1600x900",
    "X-Apps-Device": "samsung SM-G988N",
    "X-Apps-Location": "lat:59.8879617,lon:31.5165283",
    "X-Apps-Additionally": "404",
    "Accept-Encoding": "gzip, deflate, br",
}

saved_data = []

for page in range(1, 11):  # 10 страниц для получения 100 результатов
    params = {
        "sort": "popular",
        "category_id": "1",
        "page": str(page),
        "count": "10",
        "token": "9caf9be57b34aa7f7ed29b50b4fd1aba",
        "sign": "e83b4b90cc19d36b84dfbdd430c3ba0f",
    }
    
    response = requests.get(base_url, params=params, headers=headers)

    # Проверка успешности запроса
    if response.status_code == 200:
        data = response.json()  # Перевод ответа в формат JSON
        print(data.keys())
        
        for item in data['data']['goods']:
            product_info = {
                "id": item["id"],
                "name": item["title"],
                "url": item["webpage"],
                "regular_price": item["price"]["old"],
                "promo_price": item["price"]["actual"],
                "brand": item["brand_name"]
            }
            saved_data.append(product_info)
    else:
        print(f"Error on page {page}: Unable to fetch data (Status code: {response.status_code})")

# Запись данных в файл
with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(saved_data, file, ensure_ascii=False, indent=4)
