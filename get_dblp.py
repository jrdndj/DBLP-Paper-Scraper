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
