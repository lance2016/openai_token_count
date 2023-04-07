# openai_token_count
统计openai的token数量（Statistics openai token number）

## 1.安装需要的依赖

```shell
pip install -r requirements.txt
```

## 2.运行

```python
python main.py
```

## 3.调用

### 3.1 参数说明

```json
{
    "prompt": "Many words map to one token",
    "encoding_name": "p50k_base",
    "return_detail": true
}

// prompt  具体要统计token的文本
// encoding_name: 对应的模型
// return_detail: 是否返回详细信息，是则除了token数量，还会返回具体分成了哪些词，以及每个词对应的

```
### 3.2 具体调用
本地访问http://localhost:8000/count, post请求，入参为上面的参数,只有prompt是必填


## 4.参考链接

https://github.com/openai/tiktoken

