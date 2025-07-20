import typer
from pubmed_project_sudha.api import search_pubmed, fetch_papers
from pubmed_project_sudha.filter import filter_non_academic_authors
from pubmed_project_sudha.writer import write_csv, format_for_csv
from typing import Optional

app = typer.Typer()

@app.command()
def get_papers_list(
    query: str,
    file: Optional[str] = typer.Option(None, "--file", "-f", help="Output CSV filename"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output")
):
    if debug:
        typer.echo(f"Searching PubMed for query: {query}")
    ids = search_pubmed(query)
    papers = fetch_papers(ids)
    filtered_papers = []
    for p in papers:
        non_acad_auths, company_affils = filter_non_academic_authors(p)
        if non_acad_auths:
            p["NonAcademicAuthors"] = non_acad_auths
            p["CompanyAffiliations"] = company_affils
            filtered_papers.append(p)
    results = format_for_csv(filtered_papers)
    if file:
        write_csv(results, file)
        typer.echo(f"Results saved to {file}")
    else:
        import tabulate
        print(tabulate.tabulate(results, headers="keys"))

if __name__ == "__main__":
    app()