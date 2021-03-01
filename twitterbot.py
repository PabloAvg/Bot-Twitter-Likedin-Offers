from bs4 import BeautifulSoup
import requests
import tweepy
import time

CONSUMER_KEY = 'XXX'
CONSUMER_SECRET = 'XXX'
ACCESS_KEY = 'XXX'
ACCESS_SECRET = 'XXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

twitter_API = tweepy.API(auth)

for status in tweepy.Cursor(twitter_API.user_timeline).items():
    try:
        twitter_API.destroy_status(status.id)
    except:
        pass

web = requests.get('https://es.linkedin.com/jobs/search?keywords=inform%C3%A1tica&location=Madrid%2C%2BComunidad%2Bde%2BMadrid%2C%2BEspa%C3%B1a&trk=homepage-jobseeker_jobs-search-bar_search-submit&f_TP=1&sortBy=DD&f_PP=103374081&redirect=false&position=1&pageNum=0')

#print(web.content)

soup = BeautifulSoup(web.content, 'html.parser')

#print(soup.prettify())

"""
for job in soup.find_all('a'):
    if job.get('class') == ['result-card__full-card-link']:
        print(job.get('href'))

for job in soup.find_all('a'):
    if job.get('class') == ['result-card__full-card-link']:
        j = requests.get(job.get('href'))
        s = BeautifulSoup(j.content, 'html.parser')
        print(job.get_text())
        print(job.get('href'))
        for des in s.find_all('h3'):
            if des.get('class') == ['job-criteria__subheader']:
                print(des.get_text())
        for des in s.find_all('span'):
            if des.get('class') == ['job-criteria__text', 'job-criteria__text--criteria']:
                print(des.get_text())                
"""

todayJobs = []

for job in soup.find_all('a'):
    if job.get('class') == ['result-card__full-card-link']:
        oneJob = []
        j = requests.get(job.get('href'))
        s = BeautifulSoup(j.content, 'html.parser')
        oneJob.append(job.get_text())
        oneJob.append(job.get('href'))
        for des in s.find_all('h3'):
            if des.get('class') == ['job-criteria__subheader']:
                oneJob.append(des.get_text())
        for des in s.find_all('span'):
            if des.get('class') == ['job-criteria__text', 'job-criteria__text--criteria']:
                oneJob.append(des.get_text())
        todayJobs.append(oneJob)

# print(todayJobs)

def tweetJobs():
    tweet = ""
    for job in todayJobs:
        tweet += 'Nombre: '+ job[0] + "\n"
        tweet += job[2] + ': '+ job[6] + "\n"
        tweet +=job[3] + ': '+ job[7] + "\n"
        tweet += job[4] + ': ' + job[8] + "\n"
        tweet += job[5] + ': '+ job[9] + '...' + "\n"
        tweet += 'Link: '+ job[1]
        print(tweet)
        print('\n\n\n')
        twitter_API.update_status(tweet)
        tweet = ""

while True:
   tweetJobs()
   time.sleep(3600)


"""
for job in todayJobs:
    print('Nombre:', job[0])
    print(job[2] + ':', job[6])
    print(job[3] + ':', job[7])
    print(job[4] + ':', job[8])
    print(job[5] + ':', job[9] + '...')
    print('Link:', job[1])
    #print('\n\n\n')
    #twitter_API.update_status()
"""