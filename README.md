# SearchSage

SearchSage is a web application designed to enhance your search experience by providing personalized search results and summaries tailored to your demographic details. Reflecting the wisdom and insight provided by the search engine, SearchSage aims to deliver concise and relevant information that aligns with your unique profile.

## Features

- **Personalized Search**: Input your demographic details, including age, profession, gender, education level, and location, to receive search results customized to your specific profile.

- **Summarized Data**: SearchSage utilizes advanced text summarization techniques to generate concise summaries of search results, ensuring that you get the most relevant information in a digestible format.

- **Engaging User Interface**: The user interface is designed to be intuitive and user-friendly, with interactive cards displaying both original search results and their summarized versions side by side.

- **Transparent Demographic Tailoring**: Demographic details are prominently displayed at the top of the page, providing transparency about how the search results were personalized to your profile.

## How It Works

1. **Demographic Information Input**: 
   - Enter your age, profession, gender, education level, and location into the provided form.

2. **Search Query Submission**:
   - Input your search query and select the desired search engine (e.g., Google, Bing).

3. **Search Execution**:
   - SearchSage sends a request to the selected search engine's API with your query and website parameters.

4. **Search Result Parsing**:
   - The application parses the search results obtained from the search engine API, extracting relevant information such as title, text content, link, and image.

5. **Text Summarization**:
   - Using advanced text summarization techniques powered by the OpenAI API, SearchSage generates summarized versions of the search result content tailored to your demographic details.

6. **User Interface Display**:
   - Search results and their summaries are displayed as interactive cards, allowing you to compare the original and summarized content easily.

7. **Continuous Improvement**:
   - SearchSage can be further enhanced with user feedback and iterative development cycles, incorporating additional features, optimizations, and improvements based on user needs and preferences.

## Getting Started

To get started with SearchSage, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/searchsage.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file and define your environment variables (e.g., OpenAI API key).

4. Run the application:
   ```
   python app.py
   ```

5. Access the application in your web browser at `http://localhost:7000`.



## Acknowledgements

SearchSage would not be possible without the following technologies and libraries:

- Flask
- Jinja2
- OpenAI API
- HTML
- CSS

