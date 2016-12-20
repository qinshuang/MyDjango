import gevent.monkey

gevent.monkey.patch_socket()

import gevent
import urllib2
import simplejson as json

global num
num = 0


def fetch(pid):
    global num
    response = urllib2.urlopen(
        'http://www.baidu.com/home/msg/data/personalcontent?num=8&indextype=manht&_req_seqid=0x97009a4f0002c87d&asyn=1&t=1482115774372&sid=1458_21822_12897_21125_17001_21803_21553_20929')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['errNo']
    num += 1
    print('Process %s: %s' % (pid, num))
    return json_result['errNo']


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
