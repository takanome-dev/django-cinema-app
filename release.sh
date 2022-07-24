echo "⚡ Migrating DB..."
python3 manage.py migrate

echo "🌱 Loading fixtures..."
python3 manage.py loaddata movies/fixtures/movies.json
python3 manage.py loaddata movies/fixtures/genres.json