import json
import os
import copy

def delete_keys_from_dict(dict_del, keys):
    """
    Delete the keys present in the keys from the dictionary.
    Loops recursively over nested dictionaries.
    """
    dict_del1= copy.copy(dict_del)
    for k,v in dict_del1.items():
        if k in keys:
            del dict_del[k]
        if isinstance(v, dict):
            delete_keys_from_dict(v, keys)
    return dict_del

def delete_items_from_list(list_del, keys):
    """
    Delete the items present in the list.
    """
    for item in keys:
        if item in list_del:
            list_del.remove(item)
    return list_del

def delete_element_from_json(*del_elements):
    """
    Delete one or more elements from json input file. 
    Loops recursively over nested json elements.
    Created new json file
    """
    cur_dir = os.getcwd()
    with open (cur_dir+"/test_payload.json") as input_file:
       input_data = json.load(input_file)
       input_data_copy= copy.copy(input_data)
    for key,value in input_data_copy.items():
        if key in del_elements:
            del input_data[key]
        if isinstance(value, dict):
             value = delete_keys_from_dict(value, del_elements)
        if isinstance(value, list):
             value = delete_items_from_list(value, del_elements)

    with open ("modified.json", "w") as output_file:
        json.dump(input_data, output_file, indent=2)
        print (" Modified json file created successfully in this path {}".format(cur_dir+"/modified.json"))

delete_element_from_json('outParams','appdate')
