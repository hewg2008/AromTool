#只加载必要的Kekule.js中的功能模块
# 若加载整个kekule.min.js，由于kekule.min.js中特殊Unicode字符的关系，execjs编译时会报错
import execjs
import os


ROOT = os.path.dirname(os.path.realpath(__file__))

jsCode = open(ROOT+'/lib/kekule.js/root.min.js', 'r', encoding = 'utf8').read()  \
    + open(ROOT+'/lib/kekule.js/localization.min.js', 'r', encoding = 'utf8').read()  \
    + open(ROOT+'/lib/kekule.js/data.min.js', 'r', encoding = 'utf8').read()   \
    + open(ROOT+'/lib/kekule.js/common.min.js', 'r', encoding = 'utf8').read()  \
    + open(ROOT+'/lib/kekule.js/core.min.js', 'r', encoding = 'utf8').read() \
    + open(ROOT+'/lib/kekule.js/io.min.js', 'r', encoding = 'utf8').read()   \
    + open(ROOT+'/lib/kekule.js/algorithm.min.js', 'r', encoding = 'utf8').read()  \
    + open(ROOT+'/lib/kekule.js/kekule.loaded.js', 'r', encoding = 'utf8').read()
# 附加的js文件，封装获取芳香性原子信息的几个函数
jsCode += open(ROOT+'/lib/kekule.js/aromaticDetect.js', 'r', encoding = 'utf8').read()

# 编译载入的js
ctx = execjs.compile(jsCode)



def getAromaticAtomInfoOfMolList(molData):
	global ctx
	return ctx.call('getAromaticDetails', molData)  # 调用封装的js函数，返回{symbol, coord}的JSON数据