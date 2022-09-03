"""Search Engine Module"""
from typing import Dict, Any, List
import asyncio
from bs4 import BeautifulSoup
from api.core.network import fetch_html

async def search_engine(query:str, page:int, lang:str)-> Dict[str,Any]:
    """Google Search"""
    response = await fetch_html(url=f"https://www.google.com/search?q={query}&lr=lang_{lang}&start={str(page*10)}")
    urls = [link.find("a")["href"] for link in BeautifulSoup(response, "lxml").find_all("div", class_="yuRUbf")]
    summaries = [link.find("h3").text for link in BeautifulSoup(response, "lxml").find_all("div", class_="yuRUbf")]   
    return [{"url":item[0],"title":item[1]} for item in list(zip(urls, summaries))]

async def search_pypi(query:str, page:int=1)-> List[Dict[str,Any]]:
    """PyPI Search"""
    response = await fetch_html(url=f"https://pypi.org/search/?q={query}&page={page}")
    links = [f"https://www.pypi.org/{link['href']}" for link in BeautifulSoup(response, "lxml").find_all("a", class_="package-snippet")]
    tasks = [fetch_html(url=link) for link in links]
    packages = await asyncio.gather(*tasks)
    responses = []
    for p in packages:
        title = BeautifulSoup(p, "lxml").find("h1", class_="package-header__name").text.strip().split(" ")[0]
        version = BeautifulSoup(p, "lxml").find("h1", class_="package-header__name").text.strip().split(" ")[1]
        command = BeautifulSoup(p, "lxml").find("span", id="pip-command").text
        package = {"title":title,"version":version,"command":command}
        responses.append(package)
    return responses