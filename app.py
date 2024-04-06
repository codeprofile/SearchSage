from flask import Flask, render_template, request
from search_engines.google_search import search_google, parse_link
from dotenv import load_dotenv
from openai import OpenAI
import os

app = Flask(__name__)
# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_summarizer(demographic_det, long_text: str):
    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.7,
        top_p=0.5,
        frequency_penalty=0.5,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant for text summarization.",
            },
            {
                "role": "user",
                "content": f"Summarize this for a {demographic_det['person_age']} year old {demographic_det['person_profession']} {demographic_det['person_gender']}  have {demographic_det['education_level']} eduction_level and living in {demographic_det['person_location']}. The topic is {demographic_det['topic']}. Here is the text: {long_text}",
            },
        ],
    )
    summarized_content = res.choices[0].message.content
    return summarized_content


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
    demographic_details = {}
    search_results = search_google(query=query)
    result_cards = []

    for idx, result in enumerate(search_results, start=1):
        link = result['link']
        parsed_data = parse_link(link)

        if parsed_data:
            demographic_details = {
                "person_age": age,
                "person_gender": "Male",  # You can modify this based on user input
                "person_location": "New York City",  # You can modify this based on user input
                "person_profession": profession,
                "education_level": "Master's Degree",  # You can modify this based on user input
                "topic": query
            }
            summarised_content = generate_summarizer(demographic_details, long_text=' '.join(parsed_data['paragraphs']))

            card = {
                'title': parsed_data['title'],
                'paragraphs': parsed_data['paragraphs'],
                'link': parsed_data['link'],
                'image': parsed_data['image'] if parsed_data['image'] else 'static/defaultimage.jpg',
                'parsed_data': parsed_data
            }

            summarised_card = {
                'title': parsed_data['title'],
                'summarised_content': summarised_content
            }

            result_cards.append({'original_card': card, 'summarised_card': summarised_card})

    return render_template('index.html', result_cards=result_cards,demographic_details=demographic_details)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port=7000)
