import pandas as pd
from pathlib import Path
from util import json_to_df, csv_to_df, dict_save

class DatasetReader:
    def __init__(self) -> None:
        self.dataset = None

    def file_checking(self, dataset_path: str) -> bool:
        '''
        파일 검사
        :param dataset_path: 데이터셋 경로 ex) ../../test.json
        :return: 파일이 유효하고 로드되었는지 여부
        '''
        extension = Path(dataset_path).suffix.lower()

        extension_map = {
            '.csv': lambda: csv_to_df(dataset_path),
            '.json': lambda: json_to_df(dataset_path)
        }

        checking = extension_map.get(extension, None)

        # invalid_extension
        if checking is None:
            print("유효하지 않은 확장자입니다.")
            return False

        try:
            dataset = checking()
        except ValueError as ve:
            print("데이터셋이 올바르지 않습니다.")
            return False

        # NoneExist dataset
        if dataset is None:
            print("파일이 존재하지 않습니다.")
            return False

        # resetting self.dataset
        self.dataset = dataset

        return True

    def run(self) -> str:
        '''
        데이터셋 입력과 검사를 반복하여 수행
        :return : dataset_path
        '''

        # input dataset_path
        while True:
            dataset_path = input("데이터셋 경로를 입력해주세요 (.csv 또는 .json 파일): ")
            if self.file_checking(dataset_path):
                print(f"데이터셋이 성공적으로 로드되었습니다.\ndataset_path : {dataset_path}")
                break

        return self.dataset, dataset_path

if __name__ == "__main__":
    dr = DatasetReader()
    dr.run()