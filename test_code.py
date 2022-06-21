import json
import os


def test_get_folder_name():
    inp = "Data"
    assert inp == 'Data'

def test_read_file_names_of_a_folder():
    res = ['split_ae.fastq.data.json', 'split_ab.fastq.data.json', 'split_ac.fastq.data.json', 'split_ad.fastq.data.json', 'split_aa.fastq.data.json']
    lister = []
    dir_path = os.path.join(os.getcwd(), "Data")
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            lister.append(path)
    assert lister == res

def test_seqlen_adder():
    seqlen = 0
    file_list = ['split_ae.fastq.data.json', 'split_ab.fastq.data.json', 'split_ac.fastq.data.json', 'split_ad.fastq.data.json', 'split_aa.fastq.data.json']
    dir_path = os.path.join(os.getcwd(), "Data")
    for i in file_list:
        current_file = os.path.join(dir_path, i)
        print(current_file)
        if "data.json" in current_file:
            with open(current_file) as f:
                for line in f:
                    json_line = json.loads(line)
                    seqlen += json_line["seqlen"]
    test_seqlen = 1324172
    assert test_seqlen == seqlen