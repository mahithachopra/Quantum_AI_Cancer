from app.civic.civic_service import CivicService

service = CivicService()

results = service.query("EGFR")

print()

for record in results[:15]:

    print(record)