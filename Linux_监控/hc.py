#!/usr/bin/python
# coding=gbk

########################################################
# require dns.resolver 
# download url: http://www.dnspython.org/kits/1.6.0/

import datetime
import os
import smtplib
import sys
import time

#import dns.resolver
import re
import httplib
import urllib2
import urllib

httplib.HTTPConnection.debuglevel = 1

def uniqify(seq, idfun=None): 
  # order preserving
  if idfun is None:
      def idfun(x): return x
  seen = {}
  result = []
  for item in seq:
      marker = idfun(item)
      # in old Python versions:
      # if seen.has_key(marker)
      # but in new ones:
      if marker in seen: continue
      seen[marker] = 1
      result.append(item)
  return result

def get_ip():
  pipe = os.popen('ifconfig')
  data = pipe.read().strip()
  p = re.compile(r'inet addr:([\.\d]+)')
  r = p.findall(data)
  if len(r) > 0:
    return r[0]

ip = get_ip()
IP = ip

import hc_config

MAX_CPU_USED = hc_config.MAX_CPU_USED  
MAX_WA = hc_config.MAX_WA

FILTERS = hc_config.FILTERS
MIN_FREE_MB  = hc_config.MIN_FREE_MB
MAX_USED_PCT = hc_config.MAX_USED_PCT

PROCESS = hc_config.PROCESS
SITES = hc_config.SITES

MAILS = hc_config.DEFAULT_MAILS
MOBILES = hc_config.DEFAULT_MOBILES

if hc_config.MAILS.has_key(ip):
  MAILS = MAILS + hc_config.MAILS[ip]

MAILS = uniqify(MAILS)

if hc_config.MOBILES.has_key(ip):
  MOBILES = MOBILES + ',' + hc_config.MOBILES[ip]

mobiles = MOBILES.split(',')
mobiles = [x.strip() for x in mobiles]
mobiles = uniqify(mobiles)
if len(mobiles) > 0:
  MOBILES = mobiles[0]
  if len(mobiles) > 1:
    for x in mobiles[1:]:
      MOBILES = MOBILES + ',' + x

FILES = []
if hc_config.FILES.has_key(ip):
  FILES = hc_config.FILES[ip]

########################################################
def load(fname='warn.dat'):
  import pickle
  fp=open(fname)
  d2=fp.read()
  fp.close()
  o=pickle.loads(d2)
  return o

def save(obj,fname='warn.dat'):
  # save to file
  import pickle
  d2 = pickle.dumps(obj)
  fp=open(fname, 'w')
  fp.write(d2)
  fp.close()

def sendsms_no(dt,msg):
  if len(msg) > 150:
    message = msg[0:149]
  else:
    message = msg
  print 'Send to %s %s' % (dt, msg)
  f = { 'msg':message }
  m = urllib.urlencode(f) 
  #url = 'http://202.85.222.10:8686/SMSPortal/send?spid=hzqs2&pwd=hzqs0008&spno=0008&dt=%s&%s' % (dt,m)
  url = 'http://192.168.88.207:8888/OpenMas/send?merchant=qs_inner&phones=%s&%s' % (dt,m)  
  #htm = urlget(url)
  print url
  
########################################################
# for sms
def sendsms(dt,msg):
  if len(msg) > 150:
    message = msg[0:149]
  else:
    message = msg
  print 'Send to %s %s' % (dt, msg)
  f = { 'msg':message }
  m = urllib.urlencode(f) 
  #url = 'http://202.85.222.10:8686/SMSPortal/send?spid=hzqs2&pwd=hzqs0008&spno=0008&dt=%s&%s' % (dt,m)
  url = 'http://192.168.88.207:8888/OpenMas/send?merchant=qs_inner&phones=%s&%s' % (dt,m)
  htm = urlget(url)
  print htm 

def sendsms_s(msg):
  sendsms(MOBILES, msg)

def urlget2(url):
    request = urllib2.Request(url)
    handle = urllib2.urlopen(request)
    htm = handle.read()
    return htm 

def urlget(url):
  try:
    request = urllib2.Request(url)
    handle = urllib2.urlopen(request)
    htm = handle.read()
  except urllib2.HTTPError, err:
    print "urllib2.HTTPError"
    htm = str(err)
    #errno = err[0][0]
    print err
  except urllib2.URLError, err:
    print "urllib2.URLError"
    print err
    #print type(err)
    #print type([1,2,3])
    #print type( err[0])
    # comment out --begin --
    #errno = err[0][0]
    #errmsg =  err[0][1]
    #print errno, 'AAA', errmsg
    #if errno == -2:
    #  request = urllib2.Request(url)
    #  handle = urllib2.urlopen(request)
    #  htm = handle.read()
    #else:
    #  htm = str(err)
    # comment out --end--
    htm = str(err)
  except:
    htm = str(sys.exc_info())
  return htm 

########################################################
# for mail ....
#def getmx(toaddr):
#  domain = toaddr.split('@')[-1]
#  answers = dns.resolver.query(domain, 'MX')
#  if len(answers) > 0:
#    idx = random.choice(range(len(answers)))
#    mx = str(answers[idx].exchange)
#  else:
#    mx = domain
#  mx = mx.strip('.')
#  return mx
#
#def sendmail(fromaddr, toaddr, subject, body):
#  host = getmx(toaddr)
#  server = smtplib.SMTP(host)
#  #server.set_debuglevel(1)
#  #server.sendmail(fromaddr, toaddrs, msg)
#  msg = 'From: %s\nTo: %s\nSubject: %s\n\n%s\n' % (fromaddr, toaddr, subject, body)
#  server.sendmail(fromaddr, toaddr, msg)
#  server.quit()  
#
#def sendmail_s(fromaddr, toaddrs, subject, body):
#  for toaddr in toaddrs:
#    try:
#       sendmail(fromaddr, toaddr, subject, body)
#    except:
#       info = str(sys.exc_info())
#       print info
def sendmail_s(fromaddr, toaddr, subject, body):
  mail_host = '1876.cn'
  mail_port = '25'
  mail_user = 'servalarm'
  mail_pass = 'qishunkeji'
  server = smtplib.SMTP(mail_host, mail_port)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(mail_user, mail_pass)
  msg = 'From: %s\nTo: %s\r\nSubject: %s\n\n%s\n' % (fromaddr, toaddr, subject, body)
  #server.set_debuglevel(1)
  server.sendmail(fromaddr, toaddr, msg)
  server.quit()

######################################
#
# Requirement:
# General:
#       FS: free space < 5%，or < 200M
#       CPU: Usage > 70%
#
#       Log: dmesg / messages 



#文件系统               1K-块        已用     可用 已用% 挂载点
#/dev/mapper/VolGroup00-LogVol00                       14855176   3665468  10422940  27% /
#/dev/sda1               101086     10979     84888  12% /boot
#tmpfs                  1037848         0   1037848   0% /dev/shm
#/dev/mapper/VolGroup00-Home                       51735156  13732272  35374892  28% /home

def get_df_data():
  cmd = "df -k | awk '(NF > 1){ printf \"%s\\n\", $0 }(NF==1){ printf \"%s \", $0}'"
  pipe = os.popen(cmd)
  data = pipe.read().strip()
  lines = data.split('\n')
  
  mps = []
  for line in lines[1:]:
    fields = line.split()
    mp = {}
    mp['mount_point'] = fields[-1].strip() 
    mp['used'] = int(fields[-2].strip().replace('%',''))
    mp['free'] = int(fields[-3].strip())
    mp['freeM'] = int(fields[-3].strip())/1024
    mps.append(mp)
  return mps


#procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu------
#r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
#2  0      0 692900 380608 803308    0    0     1    11   20    1  0  0 99  1  0
#0  0      0 692900 380608 803308    0    0     0     0 1012   94  0  0 100  0  0

def get_vmstat_data():
  pipe = os.popen('vmstat -n 1 3')
  data = pipe.read().strip()
  lines = data.split('\n')
  
  wa = 0
  idle = 0
  for line in lines[3:]:
    fields = line.split()
    wa = wa + int(fields[-2].strip())
    idle = idle + int(fields[-3].strip())
  wa = wa / len(lines[3:])
  idle = idle / len(lines[3:])
  used = 100-wa-idle
  ret = {'wa':wa, 'idle':idle, 'used':used }
  return ret

#print 'wa=%d idle=%d used=%d' % (wa, idle, used)

def get_ip():
  pipe = os.popen('ifconfig')
  data = pipe.read().strip()
  p = re.compile(r'inet addr:([\.\d]+)')
  r = p.findall(data)
  if len(r) > 0:
    return r[0]
 
def file_data(fname):
  cmd = 'cat "%s"' % (fname)
  pipe = os.popen(cmd)
  data = pipe.read().strip()
  return data 

def get_ps_data():
  pipe = os.popen('ps -ef')
  data = pipe.read().strip()
  return data 

mail_from = 'servalarm@1876.cn'
vmstat = get_vmstat_data()
mps = get_df_data()

#########################################
#       FS: free space < 5%，or < 200M
#########################################
body = ''
for item in  mps:
  #print item
  mp = item['mount_point']
  body = body + str(item) + '\n'
  if mp not in FILTERS:
    alarm = False
    msg = '%s (%s) ' % (ip, mp)    
    if item['freeM'] < MIN_FREE_MB:
      msg = msg + 'freeM(%dM)<%dM ' % (item['freeM'],MIN_FREE_MB)
      alarm = True
    if item['used'] > MAX_USED_PCT:
      msg = msg + 'used(%d%%)>%d%%' % (item['used'],MAX_USED_PCT)
      alarm = True
    if alarm:
      sendmail_s(mail_from, MAILS, msg, msg)
      sendsms_s(msg);

#       CPU: Usage > 70%
if vmstat['used'] > MAX_CPU_USED:
  subject = '%s cpu overload %d%% > %d%% ' % (ip, vmstat['used'], MAX_CPU_USED)
  body = 'Host %s cpu overload, vmstat: %s' % (ip, str(vmstat))
  sendmail_s(mail_from, MAILS, subject, body)
  msg = '%s cpu overload %d%% > %d%% ' % (ip, vmstat['used'], MAX_CPU_USED)
  sendsms_s(msg);

if vmstat['wa'] > MAX_WA:
  subject = '%s cpu wa overload %d%% > %d%% ' % (ip, vmstat['wa'], MAX_WA)
  body = 'Host %s cpu wa overload, vmstat: %s' % (ip, str(vmstat))
  sendmail_s(mail_from, MAILS, subject, body)
  msg = '%s cpu wa overload %d%% > %d%% ' % (ip, vmstat['wa'], MAX_WA)
  sendsms_s(msg);

if PROCESS.has_key(ip):
  data = get_ps_data()
  process = PROCESS[ip]
  for proc in process:
    if data.find(proc) == -1:
      msg = '%s %s is not running' % (ip, proc)
      sendmail_s(mail_from, MAILS, msg, data)
      sendsms_s(msg)

if SITES.has_key(ip):
  sites = SITES[ip]
  for site in sites:
    name = site['site']
    url = site['url']
    magic = site['magic']
    htm = urlget(url)
    if htm == None:
      msg = "(%s) site: %s can NOT get the page %s  " % (ip, name,url) 
      sendmail_s(mail_from, MAILS, msg, msg)
      sendsms_s(msg)
    elif htm.find(magic) == -1:
      # can't find magic, error.
      # print htm
      msg = "(%s) site: %s maybe down" % (ip,name) 
      sendmail_s(mail_from, MAILS, msg, msg)
      sendsms_s(msg)

def ha_log_handle(data, fname, last_ltime=0):
  ltime = last_ltime
  lines = data.split('\n')
  err_lines = [x for x in lines if x.find('ERROR') != -1 or x.find('WARN') != -1]
  warn_lines = []
  for line in err_lines:
    fs = line.split()
    if len(fs) > 1:
      log_time = fs[1].replace('_',':').replace('/',':')
      t = log_time.split(':')
      t = [int(x) for x in t ]
      d = datetime.datetime(t[0],t[1],t[2],t[3],t[4],t[5])
      timestamp = time.mktime(d.timetuple())
      if timestamp > last_ltime:
        ltime = timestamp
        warn_lines.append(line)

  if len(warn_lines) > 10:
    for line in warn_lines[-5:]:
      msg = '%s %s %s' % (ip, fname, line)
      sendsms_s(msg)
      sendmail_s(mail_from, MAILS, msg, msg)
  else:
    for line in warn_lines:
      msg = '%s %s %s' % (ip, fname, line)
      sendsms_s(msg)
      sendmail_s(mail_from, MAILS, msg, msg)

  return ltime
       

def ora_log_handle(data,fname,last_ltime=0):
  ltime = last_ltime
  p  = re.compile(r'((Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d+ \d+:\d+:\d+ \d+)', re.DOTALL)
  rr = p.findall(data)
  if len(rr) > 0:
    start = 0
    pos = []
    for r in rr:
      pp = data.find(r[0],start)
      if pp != -1:
        pos.append(pp)
        llen = len(r[0])
        start = pp + llen
        
    fdata = [data[pos[i]:pos[i+1]] for i in range(len(pos)-1)]
    fdata.append(data[pos[-1]:])
    warns = []
    for log_item in fdata:
      #print '[%s]' % (log_item)
      rr2 = p.findall(log_item)
      if len(rr2) > 0:
        ts = rr2[0][0]
        d2 = time.strptime(ts,'%a %b %d %H:%M:%S %Y')
        t = time.mktime(d2)
        print t, ltime
        if log_item.find('ORA-') != -1 and t > ltime:
          warns.append((t, log_item[len(ts):]))
    
    for x in warns:
      t = x[0]
      line = x[1]
      tt = datetime.datetime.fromtimestamp(int(t))
      ts = tt.strftime('%m/%d_%H:%M:%S')
      msg = '%s %s %s %s' % (ip, fname, ts, line)
      sendsms_s(msg)
      sendmail_s(mail_from, MAILS, msg, msg)
      ltime = int(t)
  return ltime

FILE_HANDLES = { 'ha-log':ha_log_handle, 'ora-log':ora_log_handle }

DATA_FILE = 'file.dat'
file_objs = {}
if os.path.exists(DATA_FILE) == True:
  file_objs = load(DATA_FILE)
else:
  save(file_objs, DATA_FILE)
for file in FILES:
  fname = file['file']
  ty = file['type']
  if os.path.exists(fname) == True and FILE_HANDLES.has_key(ty):
    print 'checking ', fname
    last_mtime = 0
    last_ltime = 0
    mtime =  os.stat(fname).st_mtime
    if file_objs.has_key(fname):
      last_mtime = file_objs[fname]['mtime']
      last_ltime = file_objs[fname]['ltime']
    if mtime > last_mtime:
      print fname
      fdata = file_data(fname)
      handle = FILE_HANDLES[ty]
      ltime = handle(fdata,fname,last_ltime) 
      file_objs[fname] = {'mtime':mtime, 'ltime':ltime}
      save(file_objs, DATA_FILE)

#print data
