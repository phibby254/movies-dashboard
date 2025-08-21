import csv
import os
import pandas as pd

# Always find the CSV relative to THIS script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(BASE_DIR, "movies.csv")   # <-- corrected path
html_file = os.path.join(BASE_DIR, "movies.html")

# Read the CSV
movies = []
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movies.append(row)

# Generate HTML
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Movie List</title>
</head>
<body>
    <h1>Movies</h1>
    <ul>
"""

for movie in movies:
    html_content += f"        <li>{movie['Title']} ({movie['Genre']}) - Rating: {movie['Rating']}</li>\n"

html_content += """    </ul>
</body>
</html>
"""

# Save HTML file
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ HTML file created: {html_file}")
def get_all_movies_html():
    try:
        df = pd.read_csv('data/movies.csv')
        # Sorted films according to their rating
        df_sorted = df.sort_values(by='Rating', ascending=False)
        html = "<ul>\n"
        for index, row in df_sorted.iterrows():
            html += f" <li>{row['Title']} (Genre: {row['Genre']}) - Rating: {row['Rating']}</li>\n"
        html += "</ul>"
        return html
    except FileNotFoundError:
        return "<p>error: data/movies.csv cannot find!</p>"
if __name__ == '__main__':
    print(get_all_movies_html())

