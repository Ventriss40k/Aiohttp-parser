import asyncio
import aiohttp
from bs4 import BeautifulSoup

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def Dou_parser(session):
    # get data from url (await)
    # parse it for needed data
    # get the data in readable shape
    # returns list of normalized parsed data
    async with session.get('https://jobs.dou.ua/vacancies/?city=Київ&category=Python&exp=0-1') as data:
        html = await data.text()
    soup = BeautifulSoup(html, "lxml")
    parse = soup.find(class_="lt").find_all(class_="l-vacancy")
    result = []
    for item in parse:
        # result.append(item.text.replace(u'\t', u'').replace(u'\xa0', ' ').replace(u'\n', ''))
        result.append(item.text)
    return result

async def Djinni_parser(session):
    async with session.get("https://djinni.co/jobs/keyword-python/?exp_level=1y", ssl=False) as data:
        html = await data.text()
    soup = BeautifulSoup(html, "lxml")
    parse = soup.find(class_="list-unstyled list-jobs").find_all(class_="list-jobs__item")
    result = []
    for item in parse:
        # result.append(item.text.replace(u'\t', u'').replace(u'\xa0', ' ').replace(u'\n', ''))
        result.append(item.text)
    return result


async def main():
    async with aiohttp.ClientSession() as session:
        result= await asyncio.gather(Dou_parser(session),Djinni_parser(session))
    return result
    # create session with context manager
    # returns list with 2 lists inside with parsed normalized data


results = asyncio.run(main())


data_for_server =[]
# here we merge two lists
for i in results:
    data_for_server = data_for_server + i

