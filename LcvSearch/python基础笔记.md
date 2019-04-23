# python

###python 基础数据结构


不可变：数字(int包括bool)、字符串(str)、元组(tuple)
可变：列表(list)、字典(dict)、集合(set无序，不可重复)


###循环语句控制

1.if else elif
2.while condition: 也可结合else使用
3.for  target_list in expression_list:  //主要是用来遍历/循环 序列 或者集合、字典
     pass
eg: a = ['apple','orange','banana','grape']
for x in a:
    print(x)
*for x in range(0,10):  //控制循环次数：重点* (0,10)只表示0-9，如果想控制中间间隔则参数为3位（0,10,2）,2表示间隔数输出：0,2,4,6,8
     print (x)          //重点*(x,end='|') 可以将输出结果以|分割 在一行显示，如果不加end,则默认分行显示

示例：
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, len(a), 2):
    print(a[i], end=' | ')
# 也可以使用切片方式：
b = a[0:len(a):2]
print(b)

###python 项目组织结构

一：项目结构
****包
***模块
**类
*函数、变量

二：导入模块

1.import 模块名  //引用时候需要加上:模块名.  为了简化使用可以：import 模块名 as 自定义，引用时候使用这个 自定义.
2.from 模块名/包 import 变量/函数/模块  
如果使用到： from 模块名/包 import *，可以在被导出的模块中定义：__all__=['变量1','变量2'] 提供可以支持导出的变量

3.换行加：\ 或者使用()来包裹起来
4.__init__.py 作用：当一个包被导入的时候，__init__.py将被首先自动执行，作用控制导出模块，批量导入（在__init__.py中导入一些常用系统库，
其他模块导入__init__.py所在的这个包就可以使用常用系统库）

***重点：1.包和模块是不会被重复导入的
         2.避免循环导入

###python 函数

def funcname(parameter_list):     ***//'**kw' 表示可变关键字参数，比如(a=1,b=2)
    pass
1.参数列表可以没有，参数形式有：1.必须参数 2.关键字参数（可以打乱顺序，提升代码的可读性）3.默认参数(在函数的参数里面直接加入默认值，
**要注意非默认参数不能放在默认参数之后)，可以配合关键字参数使用
2.return value 如果没有return 则默认返回None,如果要返回多个数值，则 return value1,value2,...返回的类型为tuple。
同时可以定义多个变量来接收返回的多个结果(序列解包),不建议使用元组下标来解析结果！！


### 面向对象(类)

类最基本作用：封装

class Class():
   //在类内部可以：
   1.定义若干内部变量--数据成员--***属于类变量
   2.定义实例方法,必须在方法的()内加入self
   比如：def test(self):
             print(self.类变量)
   3.定义构造函数：必须在构造函数的()内加入self  //在实例化时候会自动调用构造函数，也可显示调用该构造函数(实用不常见)，
   构造函数只能返回None，不能返回其他类型，否则编译报错，
   比如：def __init__(self):  //构造函数的()可以加入新的变量，来辅助完成对象实例化
             pass             //在这可以初始化对象的属性，比如self.数据成员=传入的数据成员，--***属于实例变量
使用类对象时需实例化：class = Class() //*** (class.__dict__)是一个保存实例对象内部所有变量的字典，也可以查看类的字典(Class.__dict__)

   ***//实例对象的变量读取顺序：实例变量（如果没有）——>类变量（如果没有）——>父类变量
   ***self.__class__.类变量等价于Class.类变量

   4.类方法：                //建议在类方法里操作类变量，可以使用类名或实例对象来调用类方法，不建议使用实例对象调用！
   比如：@classmethod        //装饰器
         def plus_sum(cls):
             pass
			 
   5.静态方法：              //静态方法不需要强制传入参数，可以使用类名或实例对象来调用静态方法
   比如： @staticmethod      //装饰器
          def static_add(x,y):
              pass
			  
   6.成员可见性              //如果在方法名前面加__这样的双下划线则该方法对于外部实例的对象是隐藏的，无法调用
                             //但可以通过类内部方法进行调用
							 ***重点：//在构造函数中对初始化的数据成员前面加__这样的双下划线，python会自动将该数据成员名
							          //修改为_类名+数据成员名，所以外部是无法访问到的。
    python其实本身并没有对私有的访问做控制，只是通过修改名字而已。
	
   7.面向对象的三大特性：1.继承性(多继承) 2.封装性 3.多态性
                         **对于继承：推荐使用：super(Class,self).父类方法（构造函数或方法）来调用父类方法！
						 
### 正则表达式与Json
一：正则表达式

   1. 使用内置库：re----re.findall()
   2. 字符集：[]  使用说明：[abc] 匹配为a或b或c的字符，[^abc]则为取反，[a-c]匹配为a,b,c即a-c的任意字符
   3. 概括字符集：'\d' 匹配数字字符等价于[0-9],'\D' 匹配非数字字符等价于[^0-9],
   '\w' 匹配任意字母或数字字符或_等价于[A-Za-z0-9_],'\W'匹配非单词字符包括：+, (, -, ),  , \t, \n, &, *, \r, #等等
   '\s' 匹配空白字符包括：\t, \n, , \r,'\S' 匹配非空白字符
   '.' 匹配除换行符\n之外其他所有字符
   4. 数量词(默认贪婪原则，如果使用非贪婪则加?比如:{}?)：{字符数},比如：[a-z]{3,6},最小长度为3，最大为6,
   *：匹配*号前面的字符：匹配0次或无限多次
   +：匹配+号前面的字符：匹配1次或无限多次
   ?：匹配?号前面的字符：匹配0次或1次
   5.边界匹配：^代表从开始匹配，&代表从末尾匹配，比如：^\d{4,8}& 只能匹配字符长度为4-8的数字字符串
   6.组：使用()，()内的字符串称为一个组
   7.匹配模式参数：比如：re.findall('[a-z]{3,6}', a, re.I)，re.I表示忽略大小写
   8.正则替换：re.sub(),***重点：re.sub()的第二个参数可以为一个函数！！
   
二：JSON--一种轻量级的数据交换格式

   1.例如：
   import json
   json_str = '{"name":"az","age":18}'
   student = json.loads(json_str)
   得到student返回类型为字典。
   2.序列化使用：json.dumps()
     反序列化使用：json.loads()


### 高级语法与用法 

   1.枚举(python 单例):  from enum import Enum   //1.不可变 2.防止标签重复  ***IntEnum限制枚举的value值必须为整数
                                    
   eg:                               *from enum import IntEnum,unique  
   class VIP(Enum):                  *@unique
                                     *class VIP(Enum):          //可以限制重复value的枚举
    YELLOW = 1
    RED = 2
    GREEN = 3
    BLACK = 4
	
   ***重点：枚举的名字：VIP.BLACK.name，枚举类型：VIP.BLACK  
   ***重点：for v in VIP.__members__.items(): 可遍历所有的枚举属性(包括重复value的枚举)，VIP.__members__：只会显示所有枚举的名字
   通过VIP(4) 可拿到对应的枚举类型--VIP.BLACK

   2.闭包 ==函数+环境变量   ———>保存现场
   **global 关键字修饰的变量为全局变量
eg:

origin = 0


def factory(pos):
    def go(step):
        nonlocal pos       //使用关键字nonlocal 表示pos变量为非局部变量来保存前一次运行值
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


tourist = factory(origin)
print(tourist(1))
print(tourist(4))
print(tourist(7))
   
   3.匿名函数
   
   (1).lambda 表达式
   eg: f = lambda x, y: x + y
       print(f(1, 2))
   (2).三元表达式
   条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果
   eg: x if x > y else y
   (3).map(推荐使用--替代for循环)
   map(func, iter1)---func 表示函数(可以是lambda 表达式) ，iter1 表示序列(支持多个序列参数的传入比如：list_x，list_y.....)
   
   eg：
   list_x = [1, 2, 3, 4, 5, 6, 7, 8]


   def squre(x):
       return x * x


   r = map(squre, list_x)---r是一个map object
   print(list(r))
   
   *** map 配合 lambda 表达式的使用：r = map(lambda x: x * x, list_x)
   (4).reduce(需要导入：from functools import reduce)
   
   **reduce实现原理：连续调用lambda
   eg:
   q=reduce(lambda x, y: x + y, list_x)
   print(q)
   
   (5).filter(过滤，判断真假)
   filter(function, iterable)---function 表示函数(可以是lambda 表达式--表示真假的)
   eg:
   list_filter = [1, 0, 1, 0, 0, 0, 1]
   r = filter(lambda x: True if x == 0 else False, list_filter)   ---r是一个 filter object
   print(list(r))
   
   4.装饰器
   
   eg:
import time

def decorator(func):
    def wrapper(*args, **kw):    //*args--支持任意多个可变参数,'**kw' 表示可变关键字参数，比如(a=1,b=2)
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1():
    print('this is a decorator')

f1()  


### 杂记

1.使用字典代替 switch语句  ：dict.get('key','default')---其中default表示不存在对应key返回的默认值，防止程序异常

2.列表推导式：
eg:
list_x = [1, 2, 3, 4, 5, 6, 7, 8]

list_squre = [i**2 for i in list_x if i >= 5] 对列表list_x中大于等于5的数做平方返回一个新的列表

3.集合推导式：---元组和字典也支持列表推导式
eg:
set_x = {1, 2, 3, 4, 5, 6, 7, 8}

set_squre = {i*i for i in list_x if i >= 5}

print(set_squre)

4.字典推导式：
eg:
students = {
    'justin': 12,
    'kobe': 32,
    'wade': 35
}

students_reverse = {value: key for key,value in students.items()}
print(students_reverse)

5.None 空----NoneType   ***重点：判空操作使用 if a: 或者 if not a:

 ---None 对应: False
 
6.对象存在并不一定是True ，受__len__和__bool__影响

示例：
class Objectbool():

    def __len__(self):  
        return 0

    def __bool__(self):  #如果此方法存在，则对象的bool类型只受此方法的返回值影响，与__len__方法无关
        return True


print(bool(Objectbool()))

### Scrapy 爬虫
  (1).下载 scrapy :  pip install -i https://pypi.douban.com/simple/ scrapy
  (2).虚拟环境搭建 ：mkvirtualenv article_spider

**在win32下启动scrapy需要:  pip install -i https://pypi.douban.com/simple/ pypiwin32

使用scrpy爬虫技巧在cmd里：scrapy shell http://blog.jobbole.com/114397/

MySQL-python 操作库：pip install -i https://pypi.douban.com/simple/ mysqlclient
 
Elasticsearch-python 操作库：pip install -i https://pypi.douban.com/simple/ elasticsearch-dsl

暂停scrapy: 启动命令：scrapy crawl lagou -s JOBDIR=job_info/001  暂停：ctrl+c (linux下命令：kill -f main.py) 




