# ❓ 常见问题速查

## Q1: Python 版本用哪个？

**A**: 用 **Python 3.11** 或 3.12。
- 下载：https://www.python.org/downloads/
- 安装时**勾选 "Add Python to PATH"**
- 验证：终端输入 `python --version`

## Q2: VSCode 还是 PyCharm？

**A**: **新手用 VSCode**。
- 下载：https://code.visualstudio.com/
- 安装 **Python 插件**（Microsoft 出品的）
- 安装 **中文语言包**（可选）

## Q3: DeepSeek 还是 OpenAI？

**A**: **学习用 DeepSeek**。
- 便宜（输入 1 元/百万 token）
- 国产，不用担心访问问题
- API 兼容 OpenAI 格式
- 注册：https://platform.deepseek.com/

## Q4: API Key 怎么管理？

**A**: 用环境变量或 .env 文件，**绝不能硬编码到代码**。

```python
import os
api_key = os.getenv("DEEPSEEK_API_KEY")
```

记得在 .gitignore 里加 `.env`

## Q5: 代码报错怎么办？

**A**: 按这个顺序排查：
1. 看错误信息（红色那行）
2. 检查拼写（Python 大小写敏感）
3. 检查缩进（必须 4 空格或 1 Tab）
4. 检查括号引号是否配对
5. 搜索错误信息
6. **还不行 → 贴给我（Claude）**

## Q6: 卡住超过 1 小时怎么办？

**A**: **跳过**！先模仿，再理解。
- 抄一遍能跑的代码
- 改一个变量看会怎样
- 继续往后学

不要硬磕一个点。

## Q7: GitHub 怎么用？

**A**: 三步搞定。
1. 注册 GitHub 账号
2. 创建新仓库
3. 推送代码：
```bash
git init
git add .
git commit -m "首次提交"
git remote add origin https://github.com/用户名/仓库名.git
git push -u origin main
```

## Q8: 项目部署到线上难吗？

**A**: 初期**不用部署**。
- 先本地跑通
- 录演示视频
- 简历写"本地可运行"

后期用 Streamlit Cloud 免费部署。

## Q9: 学历歧视怎么办？

**A**: **用项目实力说话**。
- 简历：项目经验 > 技能列表
- GitHub 14 周绿色贡献图
- 2-3 个完整可演示项目
- 面试能讲清技术细节

专科进 AI 应用开发岗**完全可行**，关键是实力证明。

## Q10: 学完找不到工作怎么办？

**A**: **降低预期 + 加速迭代**。
- 第一份工作先入行（6-9K 也行）
- 6 个月后跳到 12-18K
- 1-2 年 18-30K
- **关键：先进 AI 行业，再涨薪**

## Q11: 跟 Claude 对话 token 爆了怎么办？

**A**: 完成大任务后**主动存档**：
> "存档：W1 周一练习做完了"

我会写入长期记忆，下次新对话无缝继续。

## Q12: 跟 Cursor 怎么配合用？

**A**: 
- **Claude**（我）：规划路线、解答概念、debug
- **Cursor**：写代码时 AI 补全（Copilot）
- **分工**：用我问"为什么这样做"，用 Cursor 写"具体怎么写"

## Q13: 工作中不会怎么办？

**A**: **正常**。入职后第一周都是懵的。
- 多问同事（不要怕丢人）
- 多查文档（这是基本功）
- 主动记录不懂的点
- 3 个月后你就会了

## Q14: 项目面试怎么讲？

**A**: 用 **STAR 法则**：
- **S**ituation：项目背景
- **T**ask：你的任务
- **A**ction：你做了什么
- **R**esult：取得了什么结果

举例：
> "我做了个人知识库问答助手（S）。用户上传 PDF 后，能用自然语言提问（T）。我用 LangChain 做了文档切片、Embedding 检索、Prompt 拼接（A）。最终准确率达到 85%，比单纯问 LLM 提升 30%（R）"

---

## 💡 还有问题？

随时在 Claude 里问，或者加到这份 FAQ 里。