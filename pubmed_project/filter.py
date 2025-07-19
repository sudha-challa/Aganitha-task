from typing import List, Dict, Tuple

COMPANY_KEYWORDS = [
    "pharma", "pharmaceutical", "biotech", "inc", "corp", "ltd", "gmbh", "s.a.", "s.r.l.", "co.", "plc", "llc", "ag"
]

ACADEMIC_KEYWORDS = [
    "university", "college", "institute", "school", "hospital", "center", "centre", "faculty", "department"
]

def is_company_affiliation(affil: str) -> bool:
    affil_lower = affil.lower()
    return any(kw in affil_lower for kw in COMPANY_KEYWORDS) and not any(kw in affil_lower for kw in ACADEMIC_KEYWORDS)

def filter_non_academic_authors(paper: Dict) -> Tuple[List[str], List[str]]:
    non_academic_authors, company_affils = [], []
    for author, affil in zip(paper["Authors"], paper["Affiliations"]):
        if is_company_affiliation(affil):
            non_academic_authors.append(author)
            company_affils.append(affil)
    return non_academic_authors, company_affils