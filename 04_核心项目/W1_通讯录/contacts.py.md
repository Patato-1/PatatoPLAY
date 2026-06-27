# W1 项目：通讯录管理

完整可运行的命令行通讯录程序。

## 功能

- ✅ 添加联系人
- ✅ 查看所有联系人
- ✅ 搜索联系人
- ✅ 删除联系人
- ✅ 数据持久化（JSON 文件）

## 运行

```bash
cd "04_核心项目/W1_通讯录"
python contacts.py
```

## 完整代码

```python
"""
通讯录管理项目
W1 周六项目作业
"""

import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """从文件加载联系人"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    """保存联系人到文件"""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def add_contact(contacts):
    """添加联系人"""
    name = input("姓名: ").strip()
    phone = input("电话: ").strip()

    if not name or not phone:
        print("姓名和电话不能为空")
        return

    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"✓ 已添加 {name}")


def show_all(contacts):
    """查看所有联系人"""
    if not contacts:
        print("(通讯录为空)")
        return

    print(f"\n共有 {len(contacts)} 个联系人:")
    for i, c in enumerate(contacts, 1):
        print(f"  {i}. {c['name']}: {c['phone']}")


def search_contact(contacts):
    """搜索联系人"""
    keyword = input("搜索关键词: ").strip()
    results = [c for c in contacts if keyword in c["name"]]

    if not results:
        print(f"没有找到 '{keyword}'")
        return

    print(f"找到 {len(results)} 个:")
    for c in results:
        print(f"  {c['name']}: {c['phone']}")


def delete_contact(contacts):
    """删除联系人"""
    if not contacts:
        print("(通讯录为空)")
        return

    show_all(contacts)
    try:
        index = int(input("删除编号: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"✓ 已删除 {removed['name']}")
        else:
            print("编号无效")
    except ValueError:
        print("请输入数字")


def main():
    """主程序"""
    contacts = load_contacts()
    print(f"已加载 {len(contacts)} 个联系人")

    while True:
        print("\n=== 通讯录管理 ===")
        print("1. 添加  2. 查看  3. 搜索  4. 删除  5. 退出")
        choice = input("选择 (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_all(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("再见！")
            break
        else:
            print("无效选择")


if __name__ == "__main__":
    main()
```

## 学习要点

1. **模块化**：每个功能拆成函数
2. **数据持久化**：用 JSON 保存到文件
3. **异常处理**：用 try-except 处理输入错误
4. **用户交互**：while 循环 + if/elif 分支
5. **字符串处理**：`.strip()` 去除空格
6. **列表操作**：append、pop、enumerate

## 拓展练习

如果基础版做完了，试着加：
- [ ] 编辑联系人
- [ ] 按姓名排序
- [ ] 导出为 CSV
- [ ] 分组（家人/同事/朋友）

## 面试怎么说这个项目

> "我做了一个命令行通讯录程序，用 Python 的 JSON 模块做数据持久化，包含了增删改查四个功能。这个项目让我熟悉了函数封装、文件 I/O 和异常处理。"

**做完推到 GitHub，README 写好截图！**