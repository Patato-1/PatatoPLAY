# 🛠 DeepSeek API 集成指南

## 基本配置

```python
import os
from openai import OpenAI

# 方式 1：用环境变量（推荐）
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 方式 2：直接传 key（仅测试用）
client = OpenAI(
    api_key="sk-xxxxx",
    base_url="https://api.deepseek.com"
)
```

## 1. 单轮对话

```python
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个友好的AI助手"},
        {"role": "user", "content": "你好"}
    ]
)
print(response.choices[0].message.content)
```

## 2. 多轮对话（带历史）

```python
messages = [
    {"role": "system", "content": "你是Python导师"}
]

while True:
    user_input = input("你: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    
    ai_message = response.choices[0].message.content
    print(f"AI: {ai_message}")
    messages.append({"role": "assistant", "content": ai_message})
```

## 3. 流式输出

```python
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "写一首关于编程的诗"}],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()  # 换行
```

## 4. JSON 结构化输出

```python
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "你是一个信息提取助手，总是返回 JSON 格式"
        },
        {
            "role": "user",
            "content": "从这句话提取人名：'张三和李四去北京开会'"
        }
    ],
    response_format={"type": "json_object"}
)

import json
result = json.loads(response.choices[0].message.content)
print(result)
```

## 5. Function Calling（Agent 用）

```python
import json

# 定义工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名"}
                },
                "required": ["city"]
            }
        }
    }
]

# 用户提问
messages = [{"role": "user", "content": "上海今天天气怎么样？"}]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    tools=tools
)

# 处理工具调用
message = response.choices[0].message
if message.tool_calls:
    tool_call = message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    
    print(f"AI 想调用: {function_name}({arguments})")
    
    # 这里实际执行函数（伪代码）
    if function_name == "get_weather":
        result = {"temperature": 25, "weather": "晴"}
    else:
        result = {}
    
    # 把结果返回给 AI
    messages.append(message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result, ensure_ascii=False)
    })
    
    # 让 AI 整理回复
    final = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    print(final.choices[0].message.content)
```

## 6. 常用参数

| 参数 | 说明 | 默认 |
|---|---|---|
| `model` | 模型名 | deepseek-chat |
| `temperature` | 随机性 0-2，越高越发散 | 1.0 |
| `max_tokens` | 最大输出 token | 4096 |
| `top_p` | 核采样 0-1 | 1.0 |
| `stream` | 是否流式输出 | False |

## 7. 错误处理

```python
from openai import OpenAI, APIError, APIConnectionError

client = OpenAI(api_key="...", base_url="https://api.deepseek.com")

try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "你好"}]
    )
    print(response.choices[0].message.content)

except APIConnectionError:
    print("网络连接错误，请检查网络")
except APIError as e:
    print(f"API 错误: {e}")
except Exception as e:
    print(f"其他错误: {e}")
```

## 8. 计算 Token 用量

```python
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "你好"}]
)

print(f"输入 token: {response.usage.prompt_tokens}")
print(f"输出 token: {response.usage.completion_tokens}")
print(f"总 token: {response.usage.total_tokens}")
```

## 9. 环境变量配置（推荐）

### Windows PowerShell
```powershell
$env:DEEPSEEK_API_KEY="sk-xxxxx"
python your_script.py
```

### 用 .env 文件
```bash
# 安装 python-dotenv
pip install python-dotenv

# 创建 .env 文件
echo "DEEPSEEK_API_KEY=sk-xxxxx" > .env

# 在 Python 中加载
from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("DEEPSEEK_API_KEY")
```

### .gitignore 必须包含
```
.env
*.key
```

## 10. 成本预估

DeepSeek 定价（约）：
- 输入：1 元/百万 token
- 输出：2 元/百万 token

学习期间每天 100 次调用 × 每次 1000 token = 10 万 token/天 ≈ 0.1-0.2 元/天
**充 10 块够用 3-6 个月**

---

## ⚠️ 注意事项

1. **API Key 不要硬编码**到代码
2. **不要上传 .env 到 GitHub**
3. **控制调用频率**，避免被限流
4. **生产环境用环境变量**，开发环境用 .env