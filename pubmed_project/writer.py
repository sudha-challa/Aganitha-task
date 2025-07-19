import pandas as pd
from typing import List, Dict

def write_csv(papers: List[Dict], filename: str):
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)

def format_for_csv(papers: List[Dict]) -> List[Dict]:
    results = []
    for paper in papers:
        non_acad_auths, company_affils = paper["NonAcademicAuthors"], paper["CompanyAffiliations"]
        results.append({
            "PubmedID": paper["PubmedID"],
            "Title": paper["Title"],
            "Publication Date": paper["Publication Date"],
            "Non-academic Author(s)": "; ".join(non_acad_auths),
            "Company Affiliation(s)": "; ".join(company_affils),
            "Corresponding Author Email": paper["CorrespondingEmail"]
        })
    return results