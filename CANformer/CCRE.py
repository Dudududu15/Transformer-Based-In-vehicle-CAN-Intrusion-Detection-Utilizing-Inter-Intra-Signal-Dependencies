from proccess import hex_bin, sort_ID, PreProcessing, sensorExtractor, crateNewData, time_sort, convert2csv, READ, read_crateNewData

import json
import time
import shutil


import os
import argparse



class Main():
    def __init__(self, setting):
        self.data = setting['data']
        self.data_path = setting['data_path']
        self.root_path = setting['root_path']
        self.method = setting['method']
    def run(self):
        print('\n')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>输入至少包括包含time,id,dlc,data>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        file_path = os.path.join(self.root_path, self.data_path)
        df = hex_bin(file_path)
        sort_ID(df)
        NewfilePath = 'sort_ID'
        Result_file = open("{}.txt".format(self.data), mode='w')
        allFile = os.listdir(NewfilePath)
        time_list = []
        output_folder = 'reverse_result'
        os.makedirs(output_folder, exist_ok=True)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>逆向开始>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        if os.listdir(output_folder):
            shutil.rmtree(output_folder)
            os.makedirs(output_folder)

        for file_name in allFile:
            start_time = time.time()
            name = file_name[0:-4]
            print(name)
            if self.method == 'READ':
                ref = READ(NewfilePath, file_name)
                print(name, ref)
                read_crateNewData(NewfilePath, file_name, ref, output_folder)
            else:
                prevResult = PreProcessing(NewfilePath, file_name)

                ref = sensorExtractor(prevResult)
                Result_file.write(name)
                Result_file.write('\r\n')
                Result_file.write(json.dumps(ref))
                Result_file.write('\r\n')
                print(name, ref)
                crateNewData(NewfilePath, file_name, ref, output_folder)

            end_time = time.time()
            if ref != []:
                time_list.append(end_time - start_time)
            else:
                time_list.append(-1)
        Result_file.close()
        time_sum = 0
        time_count = 0
        for i in time_list:
            if i != -1:
                time_sum += i
                time_count += 1
        time_cost = time_sum / time_count
        print('reverse_avg_time cost :', time_cost)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # data loader
    parser.add_argument('--data', type=str, required=True, default='CAN', help='dataset type')
    parser.add_argument('--root_path', type=str, default='./data/ETT/', help='root path of the data file')
    parser.add_argument('--data_path', type=str, default='ETTh1.csv', help='data file')
    parser.add_argument('--method', type=str, default='READ', help='reverse method')
    args = parser.parse_args()

    setting = {'data': args.data,
               'root_path': args.root_path,
               'data_path': args.data_path,
               'method': args.method}
    main = Main(setting)
    main.run()




