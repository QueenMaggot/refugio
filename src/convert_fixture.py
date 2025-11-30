# convert_fixture.py
with open("backup.json", "r", encoding="latin1") as f:
    data = f.read()

with open("backup_utf8.json", "w", encoding="utf8") as f:
    f.write(data)

print("Conversión completa: backup_utf8.json creado en UTF-8")
