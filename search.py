import json

def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    search_string = search_string.lower()
    for item in json_data:
        if any(search_string in str(value).lower() for value in item.values()):
            results.append(item)
    return results

#Step 1- converting searched words to lower case for case-insensitive results
#Step 2- Looping through JSON Data items
#Step 3- Converting Items to strings inorder to comapre with the search word, if yes retrun with results.