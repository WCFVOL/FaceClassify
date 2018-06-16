#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os


def parse_params(params_file):
    f = open(params_file, 'rb')
    lines = f.readlines()
    f.close()

    test_data_folder  = r'D:\test_result_folder'
    # lines[0].decode().split(':')[1].strip(' \n')
    train_data_folder = r'D:\train_result_folder'
    # lines[1].decode().split(':')[1].strip(' \n')
    
    len_lines = len(lines)
    i = 2
    results = []
    while i < len_lines:
        if lines[i].startswith('['.encode()):
            params = {}
            params['id'] = lines[i][1:-2]
            i += 1
            while i < len_lines:
                if lines[i] == b'\n':
                    break
                k = lines[i].decode().split(':')[0]
                v = lines[i].decode().split(':')[1]
                k = k.strip(' ')
                v = v.strip(' \n')
                params[k] = v
                i += 1
            results.append(params)
        i += 1
    return results, test_data_folder, train_data_folder

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('Usage: python %s params_file' % (sys.argv[1]))
        sys.exit()
    results, test_data_folder, train_data_folder = parse_params(sys.argv[1])
    import pprint
    pprint.pprint(results)
    print (test_data_folder)
    print (train_data_folder)



