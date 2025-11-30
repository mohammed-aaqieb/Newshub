from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

# Get your free API key from https://newsapi.org/
NEWS_API_KEY = 'c781fab947514dfab114ca7ac3bf1c83'  # Replace with your actual API key
BASE_URL = 'https://newsapi.org/v2/'

def format_date(date_str):
    if not date_str:
        return ""
    try:
        # Parse ISO format (e.g., 2023-10-27T10:00:00Z)
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%b %d, %Y')
    except ValueError:
        return date_str

app.jinja_env.filters['format_date'] = format_date

def get_news(category=None, query=None, country='us', page=1):
    """Fetch news from NewsAPI"""
    if query:
        url = f'{BASE_URL}everything?q={query}&apiKey={NEWS_API_KEY}&language=en&pageSize=20&page={page}'
    elif category:
        url = f'{BASE_URL}top-headlines?category={category}&country={country}&apiKey={NEWS_API_KEY}&pageSize=20&page={page}'
    else:
        url = f'{BASE_URL}top-headlines?country={country}&apiKey={NEWS_API_KEY}&pageSize=20&page={page}'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('articles', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

@app.route('/')
def index():
    articles = get_news()
    return render_template('index.html', articles=articles, active_category='home')

@app.route('/category/<category_name>')
def category(category_name):
    articles = get_news(category=category_name)
    return render_template('index.html', articles=articles, active_category=category_name)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '')
    articles = get_news(query=query)
    return render_template('index.html', articles=articles, active_category='search', query=query)

@app.route('/api/news')
def api_news():
    category = request.args.get('category')
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    
    articles = get_news(category=category, query=query, page=page)
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
