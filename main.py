import random
import datetime
import os

def load_quotes(file_path="quotes.txt"):
    if not os.path.exists(file_path):
        print("语录文件不存在！请先创建 quotes.txt")
        return []
    
    with open(file_path, "r", encoding="utf-8") as f:
        quotes = [line.strip() for line in f if line.strip()]
    return quotes


def get_daily_quote(quotes):
    if not quotes:
        return "今天没有鸡汤，只有摆烂～"
    
    # 用日期做种子，保证同一天返回相同的一句
    today = datetime.date.today()
    seed = today.year * 10000 + today.month * 100 + today.day
    random.seed(seed)
    
    return random.choice(quotes)


def main():
    print("═" * 50)
    print(f"今天是 {datetime.date.today().strftime('%Y年%m月%d日')}")
    print("每日一句：")
    print()
    
    quotes = load_quotes()
    quote = get_daily_quote(quotes)
    
    print(f"    {quote}")
    print()
    print("═" * 50)


if __name__ == "__main__":
    main()
