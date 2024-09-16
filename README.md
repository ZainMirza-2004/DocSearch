# Query-Based Document Search

This Python script offers a comprehensive solution for building a word dictionary, creating an inverted index, and processing text queries to find and rank relevant documents. Leveraging vector mathematics, it calculates angles between document vectors and query vectors to provide precise search results.

## Features

- **Word Dictionary**: Builds a dictionary of unique words and their counts from a given document.
- **Inverted Index**: Creates an index listing all documents associated with each word for efficient search.
- **Query Processing**: Finds and ranks relevant documents based on query content.
- **Vector Calculations**: Computes angles between document and query vectors using NumPy.

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Math](https://img.shields.io/badge/Math-000000?style=flat-square&logo=math&logoColor=white)

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/text-analysis-search-engine.git](https://github.com/ZainMirza-2004/DocSearch.git)
   ```
2. Navigate to the project directory:
   ```bash
   cd DocSearch
   ```
3. Install dependencies:
   ```bash
   pip install numpy
   ```

## Usage

1. Prepare your document and query files:
   - `docs.txt` - Contains the text documents to be indexed.
   - `queries.txt` - Contains the queries to be processed.

2. Run the script:
   ```bash
   python DocSearch.py
   ```

3. The script will output the relevant document indices and angles for each query.

## Example

Given a set of documents and queries, the script will:
- Build a word dictionary and inverted index.
- Process each query to find relevant documents.
- Calculate and print the angle between document and query vectors, ranking documents by relevance.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with improvements or bug fixes.

## Contact

For any questions or feedback, please reach out to [zainmirza3369@gmail.com](mailto:zainmirza3369@gmail.com).
