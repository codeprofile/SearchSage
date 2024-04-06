from openai import OpenAI
import os

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


#
if __name__ == "__main__":
    demographic_details = {
        "person_age": 35,
        "person_gender": "Male",
        "person_location": "New York City",
        "person_profession": "Software Engineer",
        "education_level": "Master's Degree",
        "topic" : "Data Science"
    }
    print(generate_summarizer(demographic_details,long_text=
        'Veera is a name of Indian origin, often given to both boys and girls. It means "brave" or "valiant" in '
        'Sanskrit. The name Veera is commonly found in various Indian languages such as Hindi, Tamil, Telugu, '
        'and Kannada. It symbolizes courage, strength, and determination. Veera is often associated with heroic '
        'qualities and is a popular choice for baby names in Indian families.'))
