#/**
#* @file loader.py
#* @author chenyunan (chen.yunan_01@nus.edu.sg)
#* @brief
#* @version 0.1
#* @date 2024-02-06
#*
#* @copyright Copyright (c) 2024 
#*
#*/

from datasets import load_dataset
from typing import AnyStr, List
from common import get_subset_list

class loader:
    def __init__(self,
                name : AnyStr,
                tag = None):
        self.name = name
        self.config = get_subset_list(self.name)
        self.tag = tag

    @property
    def _dataset(self) -> List:
        dataset = [load_dataset(self.name, sub) for sub in self.config] if self.tag == None else \
                  [load_dataset(self.name, sub, revision=self.tag) for sub in self.config]
        return dataset


if __name__ == '__main__':
    #test
    data_loader = loader(name="ai2_arc")
    data_loader._dataset