import json

def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    search_string = search_string.lower()  # Convert search string to lowercase for case-insensitive search
    
    # Loop through the JSON data
    for item in json_data:
       
        # Convert item values to string and check if the search string is in any of the values
        if any(search_string in str(value).lower() for value in item.values()):
            results.append(item)
          
    return results