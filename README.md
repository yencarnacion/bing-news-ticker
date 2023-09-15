# bing-news-ticker

Welcome to `bing-news-ticker`! This project provides a scrolling ticker that displays the latest news fetched from the Bing Search API.

## Features

- Display a scrolling ticker with latest news on an HTML page.
- Easy refresh mechanism to update headlines.
- Schedule automated news updates with different types of news.
  
## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- A Bing Search API Key. [Learn More & Get Yours](https://www.microsoft.com/en-us/bing/apis/bing-news-search-api)

## Setup & Configuration

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/yencarnacion/bing-news-ticker.git
   cd bing-news-ticker
   ```

2. **API Key Configuration**
   
   Open the `secret.py` file in a text editor and replace the placeholder with your Bing Search API key:

   ```python
   API_KEY = 'YOUR_API_KEY_HERE'
   ```

3. **Start the Server**

   Serve the HTML page on port 8000 using:

   ```bash
   python3 server.py
   ```

   Now, navigate to `http://localhost:8000` in your browser to see the news ticker in action!

## Update News

- **Refresh Current News**:

  To manually refresh the `headlines.json` with the latest news:

  ```bash
  python3 top-news.py
  ```

- **Automated News Loop**:

  To refresh `headlines.json` with different types of news at scheduled intervals:

  ```bash
  python3 loop.py
  ```

## Need More Information?

For more information on how to use the Bing News API, check out the YouTube video: [**Partly Cloudy: Hello News (Intro, project structure, and HTTP requests)**](https://www.youtube.com/watch?v=89ijb6NuQ-E)

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
