# DBLP-Paper-Scraper
A quick python script that lets you scrape the names of a list of authors to help you prepare your CEUR proceedings

You can automate the process of checking the DBLP footprint (publications and academic profiles) of a list of people by using the DBLP API or other tools. 

1. **DBLP API**:
   DBLP provides an API that can be used to query its database. You can send a request to search for authors by name, and the API will return the list of their publications. 
   - You would need to create a script that sends requests to the DBLP API for each person in your list.
   - The API's search endpoint allows you to query for an author's publications using their name.

   Example of an API request:
   ```http
   https://dblp.org/search/publ/api?q=<author_name>&format=bibtex
   ```
   You can replace `<author_name>` with the name of each person on your list. In this case we use a python script to get it from a txt file containing all author names separated by line breaks. 


To automate the process of querying DBLP and getting the number of papers for a list of authors, you can use Python along with its `requests` library to interact with the DBLP API. 

### Steps:

1. **Install the required Python packages**:
   You need to install the `requests` package if you haven't already. You can install it by running this command:
   ```bash
   pip install requests
   ```

2. **Create the script**:
   Below is a Python script that will:
   - Read a list of author names from a text file (`authors.txt`).
   - Query the DBLP API for each author.
   - Count the number of publications for each author.
   - Write the results to a new text file (`author_papers.txt`).

```python
import requests

def get_publication_count(author_name):
    # Construct the URL to search for the author in DBLP
    url = f"https://dblp.org/search/publ/api?q={author_name}&format=json"
    
    try:
        # Send a GET request to DBLP API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request was unsuccessful
        
        # Parse the JSON response
        data = response.json()
        
        # The number of publications is in the "hits" field
        num_papers = data['result']['hits']['@total']
        
        return num_papers
    except requests.RequestException as e:
        print(f"Error fetching data for {author_name}: {e}")
        return 0

def process_authors(input_file, output_file):
    # Read the list of authors from the input file
    with open(input_file, 'r') as infile:
        authors = infile.readlines()
    
    # Write the results to the output file
    with open(output_file, 'w') as outfile:
        for author in authors:
            author = author.strip()  # Remove leading/trailing whitespace
            if author:
                print(f"Processing {author}...")
                num_papers = get_publication_count(author)
                outfile.write(f"{author}: {num_papers} papers\n")
                print(f"Found {num_papers} papers for {author}")

if __name__ == "__main__":
    input_file = "authors.txt"  # The file containing the list of author names
    output_file = "author_papers.txt"  # The file to write the results to
    process_authors(input_file, output_file)
```

### How to Use:
1. Create a text file (`authors.txt`) with a list of author names, one per line. Example:
   ```
   John Doe
   Jane Smith
   Alice Johnson
   ```
2. Run the script. The results will be saved in `author_papers.txt`, formatted like this:
   ```
   John Doe: 120 papers
   Jane Smith: 88 papers
   Alice Johnson: 45 papers
   ```

### Example Usage:
1. Place your `authors.txt` in the same folder as the Python script.
2. Run the Python script with:
   ```bash
   python script_name.py
   ```
3. After execution, you will find the number of papers for each author in the `author_papers.txt` file.


### If you encounter some issues, please dont hesitate to reach out. 
