import csv
import json
import xml.etree.ElementTree as ET


def file_csv(file):
    try:
        with open(file, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file)
            csv_arr = []
            for row in file_reader:
                csv_arr.append(row)
            return csv_arr
    except IOError as e:
        print('ERROR - cant find file: %s' % e)


def file_json(file):
    json_arr_begin = []
    json_arr = []
    try:
        with open(file, encoding='utf-8') as r_file:
            file_reader = json.load(r_file)
            for section, commands in file_reader.items():
                for field in commands:
                    json_key_arr = []
                    json_value_arr = []
                    for key, value in field.items():
                        json_key_arr.append(key)
                        json_value_arr.append(value)
                    json_arr_begin += [json_key_arr, json_value_arr]

        #Делаем валидный список, путем очищения от лишних ['D1', 'D3', 'D2', 'M1', 'M2', 'M4', 'M3']
        json_arr += [json_arr_begin[0]]
        len_json_arr = len(json_arr_begin)
        for i in range(1, len_json_arr):
            if json_arr_begin[i] != json_arr_begin[0]:
                json_arr += [json_arr_begin[i]]
        return json_arr
    except IOError as e:
        print('ERROR - cant find file: %s' % e)


def file_xml(file):
    xml_name = []
    xml_text = []
    try:
        tree = ET.ElementTree(file=file)
        root = tree.getroot()
        for child_of_root in root.iter():
            if child_of_root.attrib:
                xml_name.append(child_of_root.attrib['name'])
            else:
                xml_text.append(child_of_root.text)
        xml_text.remove("\n    ")
        xml_text.remove("\n        ")
        xml_arr = [xml_name, xml_text]
        return xml_arr
    except IOError as e:
        print('ERROR - cant find file: %s' % e)


