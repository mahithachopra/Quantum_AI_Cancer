from app.literature.literature_service import LiteratureService

service = LiteratureService()

papers = service.retrieve(

    {},

    [

        {

            "gene":"EGFR",

            "drug":"Osimertinib"

        }

    ],

    {}

)

print(len(papers))

for p in papers[:5]:

    print()

    print(p.title)

    print(p.journal)

    print(p.year)