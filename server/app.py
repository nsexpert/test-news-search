from flask import Flask, request
from flask_cors import CORS
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()
from searchEngine import newsSearchEngine
app = Flask(__name__)
CORS = CORS(app)

@app.route('/search', methods=['POST'])
def hello():
    result = {"articles": [], "status": 'no data'}
    data = request.json
    keyword = ''
    page=1
    language = 'en'

    if 'keyword' in data:
        keyword = data['keyword']
    if 'page' in data:
        page = data['page']
    if 'language' in data:
        language = data['language']

    if keyword != '':
        current_date = datetime.now()
        last_month_date = current_date - timedelta(days=30)
        formatted_date = last_month_date.strftime("%Y-%m-%d")
        result = newsSearchEngine.get_everything(
            q=keyword, 
            sources='bbc-news,the-verge', 
            from_param=formatted_date,
            language=language['value'],
            sort_by="relevancy",
            page=page,
            page_size=10
            )
        if result['totalResults'] == 0:
            result['status'] = 'no data'
    return result

if __name__ == '__main__':
    app.run()
