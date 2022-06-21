import json
import os


class DataAggregator:
    def __init__(self) -> None:
        self.folder = self.get_folder_name()
        self.seqlen = 0

    def get_folder_name(self) -> str:
        inp = input('Folder Name : ')
        return inp

    def read_file_names_of_a_folder(self):
        lister = []
        self.dir_path = os.path.join(os.getcwd(), self.folder)
        try:
            for path in os.listdir(self.dir_path):
                if os.path.isfile(os.path.join(self.dir_path, path)):
                    lister.append(path)
            return lister
        except FileNotFoundError:
            print("No such file or directory")
            return []

    def seqlen_adder(self, file_list):
        for i in file_list:
            current_file = os.path.join(self.dir_path, i)
            print(current_file)
            if "data.json" in current_file:
                with open(current_file) as f:
                    for line in f:
                        json_line = json.loads(line)
                        self.seqlen += json_line["seqlen"]


    def main(self):
        file_list = self.read_file_names_of_a_folder()
        self.seqlen_adder(file_list)
        print(self.seqlen)

obj = DataAggregator()
obj.main()




