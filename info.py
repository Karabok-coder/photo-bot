sites = ['https://unsplash.com/napi/topics/wallpapers/photos?', 
        'https://unsplash.com/napi/topics/textures-patterns/photos?',
        'https://unsplash.com/napi/landing_pages/wallpapers/phone?',
        ]
#для передачи номера страницы
s_last_1 = 'page='
#для первых 2-х ссылок там по 10 фото скачивается
s_last_2 = '&per_page=10'
#для третий там по 20
s_last_3 = '&per_page=20'
#заголовки, чтобы сайт не думал что я бот (.)(.)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
