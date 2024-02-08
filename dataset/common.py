#/**
#* @file common.py
#* @author chenyunan (chen.yunan_01@nus.edu.sg)
#* @brief
#* @version 0.1
#* @date 2024-02-08
#*
#* @copyright Copyright (c) 2024 
#*
#*/

import requests
from bs4 import BeautifulSoup

def request_url(name):
    url = "https://huggingface.co/datasets/" + name
    response = requests.get(url)

    #parser
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_subset_list(name) -> list:
    return get_list(name, 'Subset')

def get_split_list(name) -> list:
    return get_list(name, 'Split')

def get_list(name, part) -> list:
    soup = request_url(name)
    subset_labels = soup.find_all("label", class_="block")
    filter_list = []

    for label in subset_labels:
        if part in label.get_text():
            select_element = label.find("select", class_="form-input px-2 py-1")
            if select_element:
                option_elements = select_element.find_all("option")
                for option in option_elements:
                    option_value = option["value"]
                    filter_list.append(option_value)
    return filter_list