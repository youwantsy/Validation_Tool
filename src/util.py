import pandas as pd
import os
import json
import numpy as np
import csv
from typing import Union

def csv_to_df(dataset_path:str) -> Union[None, pd.DataFrame]:
    '''
    csv 파일 읽어 dataframe화
    :param dataset_path: 데이터셋 경로
    :return: 파일이 없을땐 None, 있을땐 dataframe
    '''
    try:
        dataframe = pd.read_csv(dataset_path, dtype=object)
    except FileNotFoundError:
        dataframe = None

    return dataframe

def json_to_df(dataset_path: str) -> Union[None, pd.DataFrame]:
    '''
    json 파일 읽어 dataframe화
    :param dataset_path: 데이터셋 경로
    :return: 파일이 없을땐 None, 있을땐 dataframe
    '''
    try:
        dataframe = pd.read_json(dataset_path, dtype=object)
    except FileNotFoundError:
        dataframe = None

    return dataframe

def dict_save(dir_path: str, file_name: str, data: dict) -> None:
    '''
    dictionary save
    :param dir_path: 저장 경로
    :return:
    '''
    os.makedirs(dir_path, exist_ok=True)
    save_path = os.path.join(dir_path, file_name)

    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_parameter(obj:object, name: str):
    """
    멤버 변수 이름을 요청받아 해당하는 값을 반환
    :obj: 요청할 객체
    :name: 요청할 멤버 변수 이름
    :return: 멤버 변수 값 또는 None
    """
    try:
        param = getattr(obj, name)
    except AttributeError:
        print(f"'{name}' 멤버 변수가 존재하지 않습니다.")
        param = None

    return param

def list_comparing(list1: list, list2: list) -> dict:
    '''
    리스트 2개를 입력받아 각각의 요소 비교
    :param list1: str값 리스트
    :param list2: str값 리스트
    :return: 공통인자, list1에만 있는 인자, list2에만 있는 인자
    '''
    list1_lower = [value.lower() for value in list1]
    list2_lower = [value.lower() for value in list2]

    compare_dict = {}

    # 공통 요소
    common_elements_lower = set(list1_lower) & set(list2_lower)
    common_elements = [value for value in list1 if value.lower() in common_elements_lower] + \
                      [value for value in list2 if value.lower() in common_elements_lower]

    # list1에만 있는 요소
    list1_not_in_list2_lower = set(list1_lower) - set(list2_lower)
    list1_not_in_list2 = [value for value in list1 if value.lower() in list1_not_in_list2_lower]

    # list2에만 있는 요소
    list2_not_in_list1_lower = set(list2_lower) - set(list1_lower)
    list2_not_in_list1 = [value for value in list2 if value.lower() in list2_not_in_list1_lower]

    compare_dict["common"] = common_elements
    compare_dict["not_found_types"] = list1_not_in_list2
    compare_dict["other_types"] = list2_not_in_list1

    return compare_dict
