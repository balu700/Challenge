import json
import os

class DataAggregator:
    def __init__(self) -> None:
        self.folder = self.get_folder_name()
        self.seqlen = 0 # using seqlen as a global variable as its used in multiple places

    # method to read Folder Name as an input from the user.
    def get_folder_name(self) -> str:
        inp = input('Folder Name : ')
        return inp

    '''
    Read all the file names in a Folder
    exception is handeled, 
    if Folder exits read the file names
    else throw and exception
    '''
    def read_file_names_of_a_folder(self):
        lister = []
        # making dir_path as a global variable because its being used in many places.
        self.dir_path = os.path.join(os.getcwd(), self.folder)
        try:
            for path in os.listdir(self.dir_path):
                if os.path.isfile(os.path.join(self.dir_path, path)):
                    lister.append(path)
            return lister
        except FileNotFoundError:
            print("No such file or directory")
            return []

    '''
    Main method in which we can add all the seqlen values
    and keep the cummulative value in global variable
    self.seqlen.
    '''
    def seqlen_adder(self, file_list):
        for i in file_list:
            current_file = os.path.join(self.dir_path, i)
            print(current_file)
            if "data.json" in current_file:
                with open(current_file) as f:
                    for line in f:
                        json_line = json.loads(line)
                        self.seqlen += int(json_line["seqlen"]) # type casting is value exists as a string to int.

    # Main method to call the needed methods in an order.
    def main(self):
        file_list = self.read_file_names_of_a_folder()
        print(file_list)
        self.seqlen_adder(file_list)
        print(self.seqlen)

obj = DataAggregator()
obj.main()




