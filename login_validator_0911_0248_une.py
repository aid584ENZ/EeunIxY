# 代码生成时间: 2025-09-11 02:48:58
import scrapy
def login_validator(username, password):
    """
    用户登录验证系统
    
    参数:
    username (str): 用户名
    password (str): 密码
    
    返回:
    bool: 登录验证结果
    """
    # 假设的用户数据库
    user_database = {
        "admin": "password123"
    }
    
    # 检查用户名是否存在
    if username not in user_database:
        # 如果用户名不存在，返回False
        print("用户名不存在")
        return False
    
    # 检查密码是否正确
    if user_database[username] == password:
        # 如果密码正确，返回True
        print("登录成功")
        return True
    else:
        # 如果密码错误，返回False
        print("密码错误")
        return False

# 示例用法
if __name__ == "__main__":
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    
    result = login_validator(username, password)
    
    if result:
        print("欢迎回来!")
    else:
        print("登录失败，请重试!")