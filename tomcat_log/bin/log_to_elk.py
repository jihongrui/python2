#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"

__doc__ = '''

USE:
    python log_to_elk.py /tomcat/access_logs_dir
'''

import os
import sys
import socket

from multiprocessing.dummy import Pool as ThreadPool

from log_config import debug,info,warning,error,dir

address = ('192.168.80.80', 20514)



class Log_send(object):
    ""
    def __init__(self,path):
        ""
        self.config = os.path.join(dir,'config')
        self.url_list = set()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pool = ThreadPool()
        self.path = path
        self.files = set()

    def _save_to_config(self):
        ""
        with open(self.config,'w') as f:
            for url in self.files:
                url = '{}\n'.format(url)
                f.write(url)

    def _ret_path_file(self,dir):
        "返回一个path下所有文件的列表"
        files = set()
        path_list = os.listdir(dir)
        if path_list:
            for url in path_list:
                url = os.path.join(dir,url)
                if os.path.isdir(url) and url not in self.url_list:
                    xfiles = self._ret_path_file(url)
                    if xfiles:
                        files.update(xfiles)
                elif os.path.isfile(url):
                    files.add(url)
                else:
                    pass
            return files
        else:
            message = 'PATH {} is not file OR dir'.format(dir)
            Warning(message)
            print(message)
            return None

    def _read_file(self,file):
        ""
        try:
            with open(file) as f:
                for line in f:
                    self.s.sendto(line,address)
        except:
            message = 'ERROR From class Log_send function _read_file_send'
            print(message)
            error(message)


    def start(self):
        ""
        if os.path.exists(self.config):
            with open(self.config) as f:
                for url in f:
                    self.url_list.add(url.strip())

        files = self._ret_path_file(self.path)
        if files:
            self.files.update(files)
        self.pool.map(self._read_file,list(self.files))
        self.pool.close()
        self.pool.join()
        self.s.close()
        self._save_to_config()


if __name__ == '__main__':
    ""
#############################################################################################################
    # check path is True
    Path = []
    # argv = [1,'D:\\e\\notepy-master\\model']
    argv = sys.argv
    if argv > 2:
        Log_path = argv[1:]
        for path in Log_path:
            path = str(path).strip()
            if os.path.isdir(path) :
                Path.append(path)
            else:
                message = "{} Is Not a PATH".format(path)
                print(message)
                Warning(message)
        if len(Path) == 0 :
            message = "Not Tomcat Log Path"
            print(message)
            error(message)
            sys.exit(2)

    else:
        message = "Not Tomcat Log Path"
        print(message)
        error(message)
        sys.exit(1)

#############################################################################################################
    for path in Path:
        x = Log_send(path)
        x.start()





