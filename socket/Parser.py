# coding=utf-8
import optparse
# 从命令行解析参数
# 定义一个解析的模板
parser = optparse.OptionParser('-H <host> -p <port>')
# 添加要解析的参数，dest：表示解析后存储参数的变量名称， type：解析成哪种类型的数据， help:帮助信息
parser.add_option('-H', dest='tgt_host', type='string', help='specify target host')
parser.add_option('-p', dest='tgt_port', type='int', help='specify target port[s]')

(options, args) = parser.parse_args()
tgt_host = options.tgt_host
tgt_port = options.tgt_port

if tgt_host is None or tgt_port is None:
    print parser.usage
    exit(0)
print 'target host:%s, target port:%d' % (tgt_host, tgt_port)
