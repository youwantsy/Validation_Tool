import pandas as pd
from Dataset_reader import DatasetReader
from Data_checker import Data_checker
from util import dict_save, get_parameter

class Validation_Tool:
    def __init__(self):
        self.dataset = pd.DataFrame
        self.dataset_path = ""

    def read(self):
        dr = DatasetReader()
        dataset, dataset_path = dr.run()
        self.dataset = dataset
        self.dataset_path = dataset_path
        print(f"[dataset.head]\n{dataset.head()}")

    def check(self, save: bool):
        dc = Data_checker(dataset=self.dataset, dataset_path=self.dataset_path)
        # dataset information displaying
        dc.info_displaying()
        data_info = get_parameter(obj=dc, name="dataset_columns")

        # result_save
        if save:
            print("[Validation Tool] dataset_columns save complete!")
            dict_save(dir_path='../save', file_name='dataset_information.json', data=data_info)

        # type_checking
        dc.type_checking()

def main():
    tool = Validation_Tool()
    tool.read()
    tool.check(save=True)

if __name__ == "__main__":
    main()