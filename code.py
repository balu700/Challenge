import os


class DataAggregator:
    def __init__(self) -> None:
        self.folder = self.get_folder_name()
        # self.folder_path = None

    def get_folder_name(self):
        inp = input('Folder Name : ')
        print(inp)
        return inp

    # def get_folder_path(self):
    #     inp = input('Folder path : ')
    #     print(inp)
    #     return inp

    def read_file_names_of_a_folder(self):
        lister = []
        dir_path = os.path.join(os.getcwd(), self.folder)
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                lister.append(path)
        return lister

    def main(self):
        file_list = self.read_file_names_of_a_folder()
        


obj = DataAggregator()
obj.main()




