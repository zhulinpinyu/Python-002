import requests
from bs4 import BeautifulSoup as bs

def get_movies_url():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Cookie': '__mta=51272342.1595578571207.1595578603793.1595578669279.5; uuid_n_v=v1; uuid=EDD78390CD8511EA8AF6570E3933DABA25EBEA8014A048379ECCB31D2388E323; _csrf=d5f48b2a2327a8689869e6cc33b1b21a1e0f6db700298abcc678b3245fca551a; _lxsdk_cuid=1737fe4d774c8-0b3f8041caebee-15356650-13c680-1737fe4d774c8; _lxsdk=EDD78390CD8511EA8AF6570E3933DABA25EBEA8014A048379ECCB31D2388E323; mojo-uuid=e2d7239259a9da63d21596b4723989d5; mojo-session-id={"id":"5043b9cca45bdf949ff15a5c6ad0fd22","time":1595578571229}; mojo-trace-id=8; __mta=51272342.1595578571207.1595578669279.1595579224054.6; _lxsdk_s=1737fe4d775-5e2-de8-589%7C%7C14'
    }
    url = "https://maoyan.com/films?showType=3"
    res = requests.get(url, headers=headers)
    movie_items = bs(res.text, 'html.parser').find_all('div', attrs={'class': 'movie-hover-info'})[0:10]
    for movie in movie_items:
        [name_html, tag_html, _, plan_date_html] =  movie.find_all('div', attrs={'class': 'movie-hover-title'})
        name = name_html.find('span', attrs={'class': 'name'}).text
        tag = tag_html.text.split(':\n')[1].strip()
        plan_date = plan_date_html.text.split(':\n')[1].strip()
        with open('./movies.csv', 'a+', encoding='utf-8') as f:
            f.write(f"\"{name}\", \"{tag}\", \"{plan_date}\"\n")

get_movies_url()