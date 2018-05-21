# PROTOBUF

这个目录是配合[javatech](https://github.com/gino2010/javatech)中的[protobuf](https://github.com/gino2010/javatech/tree/master/grpc/protobuf)工程的，
来展示跨语言的序列化和反序列化。

This directory works with [protobuf](https://github.com/gino2010/javatech/tree/master/grpc/protobuf) in [javatech](https://github.com/gino2010/javatech), 
to demonstrate cross-language serialization and deserialization. 

###Tips
在当前目录运行

Run in current directory

```
protoc addressbook.proto --python_out=./ 
```

生成python对象结构文件

generate python object structure file