import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL of the website
url = "https://ipm.ucanr.edu/PMG/diseases/diseaseslist.html"  

url_test = "https://ipm.ucanr.edu/PMG/GARDEN/FLOWERS/DISEASE/dryrot.html"

# Step 2: Send a GET request to the website
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Step 5: Extract the required information
    # Example: Extracting all table rows (tr) and columns (td) from a table
    table = soup.find("table")  # Find the table element
    rows = table.find_all("tr")  # Find all rows in the table

    # Step 6: Create a list to store the extracted data
    data = []
    counter = 0
    # Step 7: Loop through the rows and extract the columns
    for row in rows:
        if counter==2:
            break
        columns = row.find_all("td")  # Find all columns in the row

        if columns:  # Skip header rows or empty rows
        #     # Extract text from each column
            row_data = [col.text.strip() for col in columns]
            print(len(row_data))

        #     # Extract the link from the 2nd column
            link = columns[1].find("a")  # Find the <a> tag in the 2nd column
            if link:
                link_url = "https://ipm.ucanr.edu" + str(link["href"])  # Get the href attribute (the link)
        #         # Follow the link and scrape its contents
                link_response = requests.get(link_url)
                if link_response.status_code == 200:
                    link_soup = BeautifulSoup(link_response.content, "html.parser")
                    # Extract the content from the linked page (example: all paragraphs)
                    main_content = link_soup.find("div", class_="main-content")
                    if main_content:
                        # Extract all text from the main content area
                        center_body_text = main_content.get_text(separator=" ", strip=True)
                        row_data.append(center_body_text)
                    else:
                        row_data.append("Section not found")
                else:
                    row_data.append("Failed to retrieve link content")  # Handle failed requests
            else:
                row_data.append("No link found")  # Handle rows without links

            data.append(row_data)

        counter += 1
        # row_data = [col.text.strip() for col in columns]  # Extract text from each column 
        # if row_data:  # Skip empty rows ----
        #     data.append(row_data) 

    # Step 8: Create a DataFrame using pandas
    df = pd.DataFrame(data, columns=["plant_crop", "common_name", "scientific_name", "type", "health_guide"])
    print(df.shape)
    print(df.head(10))

    print(df["health_guide"][0])

    # Step 9: Save the DataFrame as a CSV file
    # df.to_csv("extracted_data.csv", index=False, header=False)  # Save as CSV file
    # print("Data saved to extracted_data.csv")

    # get the context from the link in the table

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# test url
response = requests.get(url_test)
soup = BeautifulSoup(response.content, "html.parser")
para = soup.find_all('p')
meaningful_paragraphs = []
# print(len(para))
# for p in para:
#     print(p)
    # Skip empty paragraphs
    # if not p.text.strip():
    #     continue
    # text = p.get_text(strip=True)
    # print(text)
    # if len(text) > 20 and not any(keyword in text.lower() for keyword in ['copyright', 'contact', 'nondiscrimination', 'accessibility']):
    #     meaningful_paragraphs.append(text)
# content = '\n'.join(meaningful_paragraphs)

# print(content)
solutions_header = soup.find('strong', string='Solutions')
print(solutions_header)
# Initialize an empty list to hold relevant content
relevant_texts = []

if solutions_header:
    # Get the parent of the <strong> tag, which is likely <p>
    parent = solutions_header.parent
    print(parent)
    # Append the 'Solutions' paragraph
    relevant_texts.append(parent.get_text(strip=True))
    # Find the next sibling <p> (the content after 'Solutions')
    next_p = parent.find_next_sibling('p')
    while next_p:
        relevant_texts.append(next_p.get_text(strip=True))
        next_p = next_p.find_next_sibling('p')

# Join the collected texts
main_content = '\n'.join(relevant_texts)

print(main_content)


# import requests
# from bs4 import BeautifulSoup

# # URL to scrape
# url = "https://ipm.ucanr.edu/PMG/GARDEN/FRUIT/DISEASE/shothole.html"

# # Fetch the page
# response = requests.get(url)
# response.raise_for_status()  # Ensure we notice bad responses

# # Parse HTML
# soup = BeautifulSoup(response.text, "html.parser")

# # Find the main content area (usually in <div id="main"> or similar)
# # On this site, the main content is inside <div id="main_body">
# main_content = soup.find("div", id="main_body")
# if not main_content:
#     main_content = soup  # fallback to whole soup

# # Find all headings and paragraphs
# headings = main_content.find_all(['h2', 'h3', 'b'])
# results = {}

# # We will look for headings that mention the disease issue and solution
# target_keywords = {
#     "issue": ["attacks", "symptoms", "disease", "rot", "problem", "description"],
#     "solution": ["solution", "control", "management", "prevent", "avoid", "treatment"]
# }

# def heading_matches(heading, keywords):
#     text = heading.get_text().lower()
#     return any(kw in text for kw in keywords)

# # Find relevant sections
# for heading in headings:
#     text = heading.get_text().strip().lower()
#     # Check if this heading is about the issue
#     if heading_matches(heading, target_keywords["issue"]):
#         # Get the next sibling paragraphs
#         issue_paras = []
#         sibling = heading.find_next_sibling()
#         while sibling and sibling.name == "p":
#             issue_paras.append(sibling.get_text().strip())
#             sibling = sibling.find_next_sibling()
#         results['Issue'] = "\n".join(issue_paras)
#     # Check if this heading is about the solution
#     if heading_matches(heading, target_keywords["solution"]):
#         solution_paras = []
#         sibling = heading.find_next_sibling()
#         while sibling and sibling.name == "p":
#             solution_paras.append(sibling.get_text().strip())
#             sibling = sibling.find_next_sibling()
#         results['Solution'] = "\n".join(solution_paras)

# # Fallback: If headings are not found, extract the first few paragraphs
# if not results:
#     paragraphs = main_content.find_all("p")
#     if paragraphs:
#         results['Issue'] = paragraphs[0].get_text().strip()
#         if len(paragraphs) > 1:
#             results['Solution'] = paragraphs[1].get_text().strip()

# # Print the results
# print("=== Issue of the Disease ===")
# print(results.get('Issue', 'Not found'))

# print("\n=== Solution ===")
# print(results.get('Solution', 'Not found'))
