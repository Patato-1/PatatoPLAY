"""
通讯录管理项目
W1 周六项目作业

功能：
1. 添加联系人
2. 查看所有联系人
3. 搜索联系人
4. 删除联系人
5. 数据持久化（保存到 JSON 文件）
"""

import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """从文件加载联系人列表"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    """保存联系人列表到文件"""
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
    keyword = input("请输入搜索关键词: ").strip()
    results = [c for c in contacts if keyword in c["name"]]

    if not results:
        print(f"没有找到包含 '{keyword}' 的联系人")
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
        index = int(input("请输入要删除的编号: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"✓ 已删除 {removed['name']}")
        else:
            print("编号无效")
    except ValueError:
        print("请输入有效数字")


def main():
    """主程序"""
    contacts = load_contacts()
    print(f"已加载 {len(contacts)} 个联系人")

    while True:
        print("\n=== 通讯录管理 ===")
        print("1. 添加联系人")
        print("2. 查看所有")
        print("3. 搜索")
        print("4. 删除")
        print("5. 退出")
        choice = input("请选择 (1-5): ").strip()

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
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()