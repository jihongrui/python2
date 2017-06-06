#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "15315731537@qq.com"

import os


def read_conf(file):
    "read nginx config file , return list [server_name,proxy_pass]"
    file_list = []
    with open(file) as f:
        for line in f:
            if '#' not in line :
                line = line.replace(';','')
                line = line.strip().split()
                if 'server_name' in line:
                    file_list.append(line[1:])
                elif 'proxy_pass' in line:
                    file_list.append(line[1:])
                else:
                    pass
    return file_list


def get_all_domain():
    "read all nginx config file, return a dict {config_file_name:[server_name,proxy_pass]}"
    all_list = {}
    dir = 'conf.d'
    file_list = os.listdir(dir)
    for file in file_list:
        all_list[file.__str__()] = read_conf(os.path.join(dir, file))
    return all_list

def write_file(msg):
    with open('domain.txt','a+') as f:
        f.write('{} \n'.format(msg))


if __name__ == '__main__':
    ""

    all_list = get_all_domain()
    ips = set()  # Server IP

    http_ip = set()  # http proxy

    for k,v in all_list.items():
        http_p = v[-1][0]
        if http_p != '_':
            http_ip.add(http_p)
            ip = str(http_p).split(':')[1].replace('//','')
            ips.add(ip)



    ipd = {}
    ip_dict = {}
    for i in ips:
        ipd[i] = []
    for i in http_ip:
        ip_dict[i] = []

    for k,v in all_list.items():
        key = v[-1][0]
        domain = v[0]
        if key in ip_dict.keys():
            ip_dict[key].extend(domain)
    for i in ipd.keys():
        for k,v in ip_dict.items():
            if i in k:
                ipd[i].append(k)
                ipd[i].append(v)
    for k,v in ipd.items():

        write_file(k)
        write_file('{}'.format('-'*100))
        while v:
            var = v.pop(0)
            if type(var) == str:
                write_file('    http_proxy : {}'.format(var))
            elif type(var) == list:
                for q in var:
                    write_file('        {}'.format(q))
                write_file('\n')

            else:
                pass

        write_file('{}'.format('#'*100))
























