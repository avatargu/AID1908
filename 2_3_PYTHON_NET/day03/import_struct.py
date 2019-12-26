"""
struct模块

将一组简单数据进行打包，转换为bytes格式数据进行发送。或者将一组bytes格式数据进行解析。

标准：网络字节序

接口：
struct.Struct(fmt)
功能：生成结构化对象
参数：定制的数据结构

struct.pack(fmt,v1,v2,v3...)

struct.unpack(fmt,bytes_data)

st.pack(v1,v2,v3,...)
功能：将一组数据按照指定格式打包，转换为bytes字节串
参数：要打包的数据
返回值：bytes字节串

st.uppack(bytes_data)
功能：将bytes字节串按照指定格式解析
参数： 要解析的bytes字节串
返回值： 数据元组
"""
import struct

# 第一种
st = struct.Struct("i9sf")
data_pack = st.pack(1,"秦般弱".encode(),1.65)
print(data_pack)
data_unpack = st.unpack(data_pack)
print(data_unpack)
print(data_unpack[1].decode())

# 第二种
# data_p = struct.pack("i9sf",1,"秦般弱".encode(),1.65)
# print(data_p)
# data_u = struct.unpack("i9sf",data_p)
# print(data_u)
# print(data_u[1].decode())
