import pandas as pd
import os
import argparse
from argparse import Namespace

class Data_checker:
    '''
    데이터셋을 입력받아 각 항목별 범위, 타입 검사도구
    '''
    def __init__(self, dataset: pd.DataFrame, dataset_path: str) -> None:
        self.dataset = dataset
        self.dataset_path = dataset_path
        self.dataset_length = 0
        self.dataset_keys = []
        self.dataset_columns = {}

    def info_displaying(self):
        '''
        데이터셋의 정보 전시
        전시되는 정보 : 데이터셋의 길이, 컬럼 정보, 항목 별 데이터 타입
        :return:
        '''
        dataset = self.dataset
        dataset_columns = {}

        # display dataset_length
        dataset_columns["dataset_path"] = self.dataset_path
        dataset_columns["dataset_length"] = len(dataset)
        self.dataset_length = len(dataset)

        # display dataset_columns and type
        dataset_keys = dataset.keys()
        self.dataset_keys = dataset_keys

        # dtype checking per dataset_keys
        for idx, column in enumerate(dataset_keys):
            # in python, they cannot detect "NaN" only pd.isna() can detect
            # in pandas, int, float -> float | int, str, float -> int, str, float | NaN -> float
            dtypes = [type(None).__name__ if pd.isna(value) else type(value).__name__ for value in dataset[column]]
            unique_dtypes = list(set(dtypes))
            dataset_columns[column] = unique_dtypes

        # update dataset_columns
        self.dataset_columns = dataset_columns

    def round_checking(self):
        '''
        데이터 항목 별 범위 체크
        :return:
        '''
        pass

    def type_checking(self):
        '''
        데이터타입 체크
        :return:
        '''
        # 데이터의 컬럼 하나씩 돌아가면서 사용자가 입력한 타입으로 존재하는지 확인
        dataset = self.dataset
        columns = dataset.keys()
        for idx, column in enumerate(columns):
            print(f"[column '{idx}' : '{column}']")
            required_type = input(f"'{column}'의 데이터 타입을 입력해주세요 (예: str, int, float) : ")

            input_types = [typ.replace(' ', '') for typ in required_type.split(',')]
            input_types = list(set(input_types)) # 중복 제거
            input_types = list(filter(None, input_types)) # 빈 값 제거

            # column의 data_types 체크
            dtypes = [type(None).__name__ if pd.isna(value) else type(value).__name__ for value in dataset[column]]
            unique_dtypes = list(set(dtypes))
            print(f"입력: {input_types}\n"
                  f"타입: {unique_dtypes}")

        pass

if __name__ == "__main__":
    dataset = pd.read_json('test.json')
    dc = Data_checker(dataset=dataset)
