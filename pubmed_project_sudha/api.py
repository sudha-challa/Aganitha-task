import requests
from typing import List, Dict

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def search_pubmed(query: str, retmax: int = 200) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }
    resp = requests.get(PUBMED_SEARCH_URL, params=params)
    resp.raise_for_status()
    id_list = resp.json()["esearchresult"]["idlist"]
    return id_list

def fetch_papers(ids: List[str]) -> List[Dict]:
    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    resp = requests.get(PUBMED_FETCH_URL, params=params)
    resp.raise_for_status()
   
    from xml.etree import ElementTree as ET
    root = ET.fromstring(resp.content)
    papers = []
    for article in root.findall(".//PubmedArticle"):
           
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or article.findtext(".//PubDate/MedlineDate")
        authors = []
        affiliations = []
        emails = []
        for author in article.findall(".//Author"):
            last = author.findtext("LastName") or ""
            fore = author.findtext("ForeName") or ""
            full_name = f"{fore} {last}".strip()
            affil = author.findtext("AffiliationInfo/Affiliation") or ""
            email = ""
            if "@" in affil:
                for word in affil.split():
                    if "@" in word:
                        email = word
                        break
            authors.append(full_name)
            affiliations.append(affil)
            emails.append(email)
        corr_email = next((e for e in emails if e), "")
        papers.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Authors": authors,
            "Affiliations": affiliations,
            "CorrespondingEmail": corr_email
        })
    return papers