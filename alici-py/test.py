import psycopg2
conn = psycopg2.connect("postgresql://neondb_owner:npg_YA5DVX0fvWrg@ep-frosty-shape-a8fhb2m2-pooler.eastus2.azure.neon.tech/neondb?sslmode=require")
print("Conexão ok!")
