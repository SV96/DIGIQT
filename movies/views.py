from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from bs4 import BeautifulSoup as bs
import requests
from movies.models import scrapdata

from django.http import HttpResponse  # return response
from django.shortcuts import get_object_or_404  # get object else not found
from rest_framework.views import APIView  # return APIDATA
from rest_framework.response import Response  # used for return response
from rest_framework import status  # send back status
from .serializers import scrapdataSerializers,scrapdataTitleSerializers,scrapdataRateingSerializers,scrapdataReleaseSerializers,scrapdataDurationSerializers,scrapdataDescriptionSerializers


# Create your views here.
def add_data(request):
    # scrapping starts
    url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
    website = requests.get(url)
    print(website.status_code)
    soup = bs(website.content, 'lxml')
    table_row = soup.find_all('td', class_='titleColumn')

    all_movies_id = []
    for i in range(len(table_row)):
        all_movies_id.append(table_row[i].find('a').get('href'))

    all_movies_url = []
    for ami in all_movies_id:
        all_movies_url.append(
            f"https://www.imdb.com{ami}?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=M5V1K540D3TE1HMH6208&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1")

    movies_title = []
    movies_rating = []
    movies_release_data = []
    movies_duration = []
    movies_description = []

    for i in range(len(all_movies_url)):
        movie_1 = all_movies_url[i]
        movie_website = requests.get(movie_1)
        movie_soup = bs(movie_website.content, 'lxml')
        movies_title.append(movie_soup.find('div', class_='title_wrapper').find('h1').text.replace(u'\xa0', u' '))
        movies_rating.append(movie_soup.find('div', class_='ratingValue').find('span').text)
        movies_release_data.append(
            movie_soup.find('div', class_='subtext').find('a', title='See more release dates').text.rstrip("\n"))
        movies_duration.append(movie_soup.find('div', class_='subtext').find('time').text.strip())
        movies_description.append(movie_soup.find('div', class_='summary_text').text.strip())

    # scrapping ends

    for i in range(len(all_movies_url)):
        movie = scrapdata(title=movies_title[i], rating=movies_rating[i], release_date=movies_release_data[i],
                          duration=movies_duration[i], description=movies_description[i])
        movie.save()
    return render(request, "home.html")


class new_show(TemplateView):
    template_name = 'home.html'


class movieTitle(APIView):
    def get(self, request):
        movie1 = scrapdata.objects.values('title').order_by('title')
        serializer = scrapdataTitleSerializers(movie1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class movieReateing(APIView):
    def get(self, request):
        movie1 = scrapdata.objects.values('rating')
        serializer = scrapdataRateingSerializers(movie1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class movieRelease(APIView):
    def get(self, request):
        movie1 = scrapdata.objects.values('release_date').order_by('release_date')
        serializer = scrapdataReleaseSerializers(movie1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class movieDuration(APIView):
    def get(self, request):
        movie1 = scrapdata.objects.values('duration')
        serializer = scrapdataDurationSerializers(movie1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class movieDescription(APIView):
    def get(self, request):
        movie1 = scrapdata.objects.values('description')
        serializer = scrapdataDescriptionSerializers(movie1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class movieList(APIView):
    def get(self, request):
        movie1 = scrapdata.objects.all()
        serializer = scrapdataSerializers(movie1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
