from flask import Flask, render_template, request
from search_engines.google_search import search_google,parse_link
from dotenv import load_dotenv


app = Flask(__name__)
# Load environment variables from .env file
load_dotenv()




@app.route('/')
def index():
    return render_template('user_profile.html')


@app.route('/search', methods=['POST'])
def search():
    age = request.form.get('age')
    profession = request.form.get('profession')
    query = request.form.get('query')
    engine = request.form.get('engine')
    website = request.form.get('website')

    print(f"Age: {age}, Profession: {profession}, Query: {query}, Engine: {engine}, Website: {website}")

    search_results = search_google(query=query)
    result_cards = []

    for idx, result in enumerate(search_results, start=1):
        link = result['link']
        parsed_data = parse_link(link)

        if parsed_data:
            card = {
                'title': parsed_data['title'],
                'paragraphs': parsed_data['paragraphs'],
                'link': parsed_data['link'],
                'image': parsed_data['image'] if parsed_data['image'] else 'static/defaultimage.jpg'
            }
            result_cards.append(card)

    return render_template('index.html', result_cards=result_cards)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port=7000)
