import bibtexparser
from ruamel.yaml import YAML

yaml = YAML()

# Load the BibTeX file
with open('my_publications.bib', 'r') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Prepare YAML entries
publication_entries = []
for entry in bib_database.entries:
    # Extract data
    title = entry.get('title').replace('{','').replace('}','')
    authors = entry.get('author').split(' and ')  # Split authors by 'and' in BibTeX format
    date = entry.get('year')
    journal = entry.get('journal')

    for i, author in enumerate(authors):
        authors[i] = author.strip()
        if 'prajeesh' in author.lower():
            authors[i] = f'**{author}**'

    # Format for rendercv
    publication_entry = {
        'title': title.strip('{}'),  # Remove braces around title if present
        'authors': authors,
        'date': date,
        'journal': journal,
    }
    publication_entries.append(publication_entry)

publication_entries = sorted(publication_entries, key=lambda x: x['date'], reverse=True)

# Output to YAML format
with open('CV.yaml', 'r') as yaml_file:
    main_cv = yaml.load(yaml_file)

main_cv['cv']['sections']['publications'] = publication_entries
print(main_cv)
with open('Prajeesh_Ag_CV.yaml', 'w') as yaml_file:
    yaml.dump(main_cv, yaml_file)
