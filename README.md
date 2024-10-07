# Music Genre Scraping Project

In this project, **6,291 music genres** were scraped, each containing **200 songs**. For each song, the following attributes are provided:

- **Ranking Position**
- **Song Title**
- **Artist**
- **Genre**

## Data Sources

Genres were obtained from [Every Noise](https://www.everynoise.com/). For each genre, a playlist containing **200 songs** was downloaded using the [Spotify API](https://developer.spotify.com/).

## Scraping Scripts

This repository contains scripts to scrape data from the internet and then transform it into a format that can be easily imported into a database.

### Scraping data from the internet

1. Install Scrapy:  
   pip install scrapy

2. Run the scraping scripts in the following order:

scrapy runspider genrespider -o genres.jl
scrapy runspider songs.py -o data/songs.jl

### Transforming data to CSV format
Run the Python scripts in the /csv_scripts folder in any order. They will generate output files with corresponding names in the /data/csv folder.

### Usage
The complete code for the project is available in this repository, allowing you to explore and study the implementation.
