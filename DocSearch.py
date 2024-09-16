import numpy as np
import math

def word_dictionary(file_path):
    # Builds a dictionary of unique words and their counts from a given file.
    word_dict = {}
    with open(file_path, "r") as file_object:
        for line in file_object:
            words_list = line.split()
            for word in words_list:
                word_dict[word] = word_dict.get(word, 0) + 1
    print(f"Words in dictionary: {len(word_dict)}")
    return word_dict

def inverted_index(document_file):
    # Builds an inverted index listing all the documents associated with each word in the dictionary.
    inverted_index = {}
    with open(document_file, "r") as document_obj:
        for index, line in enumerate(document_obj, start=1):
            words_list = line.split()
            for word in set(words_list):  # Use set to remove duplicate words in a document
                if word in inverted_index:
                    inverted_index[word].append(index)
                else:
                    inverted_index[word] = [index]
    return inverted_index

def process_queries(query_file, document_file, word_dictionary, inverted_index):
    # Processes queries from a given file and prints relevant document indices and angles.
    with open(query_file, "r") as query_file_obj:
        for query in query_file_obj:
            print(f"Query: {query.strip()}")
            relevant_docs = find_relevant_docs(query.strip(), inverted_index)
            print(f"Relevant Documents: {' '.join(map(str, relevant_docs))}")
            calculate_angles(relevant_docs, query.strip(), document_file, word_dictionary)

def find_relevant_docs(query, inverted_index):
    # Finds the indices of documents that contain all the words in the query.
    relevant_docs = set()
    for word in query.split():
        if word in inverted_index:
            if not relevant_docs:
                relevant_docs.update(inverted_index[word])
            else:
                relevant_docs.intersection_update(inverted_index[word])
    return list(relevant_docs)

def calculate_angles(relevant_docs, query, document_file, word_dictionary):
    # Calculates the angle between the document vector and query vector for relevant documents.
    with open(document_file, "r") as document_obj:
        angles_dict = {}
        for index, line in enumerate(document_obj, start=1):
            if index in relevant_docs:
                line_dict = word_vector(line, word_dictionary)
                line_vec = list(line_dict.values())
                query_vec = [1 if word in query.split() else 0 for word in word_dictionary]
                line_array = np.array(line_vec)
                query_array = np.array(query_vec)
                angles_dict[index] = calculate_angle(line_array, query_array)
        sorted_angles = sorted(angles_dict.items(), key=lambda x: x[1])
        for doc_index, angle in sorted_angles:
            print(f"{doc_index} {angle:.5f}")

def word_vector(text, word_dictionary):
    # Builds a word vector from the given text using the word dictionary.
    word_vec = {word: 0 for word in word_dictionary}
    for word in text.split():
        if word in word_dictionary:
            word_vec[word] += 1
    return word_vec

def calculate_angle(x, y):
    # Calculates the angle between two vectors.
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

document_file = "docs.txt"
query_file = "queries.txt"

word_dict = word_dictionary(document_file)
index = inverted_index(document_file)
process_queries(query_file, document_file, word_dict, index)
