import json

with open('user_data.json', 'r', encoding='utf-8-sig') as f:
    user_data = json.load(f)


def Introduction_Print():
    intro = 'hi'
    return intro


# 測驗開始
def Test(user_id):
    return 're'


# 測驗紀錄
def Test_Record(user_id):
    return 're'


# 心得回饋
def Experience(user_id, text):  # text = 我的心得:填入心得

    # 檢查是否已經註冊
    if user_id not in user_data.keys():
        return '鑷子找不到你QQ，請輸入註冊兩字進行註冊'
    else:
        text = text.split('我的心得:')
        user_data[user_id]['experience'] = text[1]

        with open('user_data.json', 'w', encoding='utf-8-sig') as f2:  # json.dump()將資料寫成json檔案
            json.dump(user_data, f2, ensure_ascii=False, indent=4)
            f2.close()

        return '鑷子感謝您的分享\n｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡'


def Register(user_id, text):  # 姓名:填入姓名/學號:填入學號

    text = text.split('姓名:')
    text[1] = text[1].split('/學號:')
    name = text[1][0]
    student_id = text[1][1]

    # 註冊新資料
    user_data[user_id] = {
        "name": name,
        "student_id": student_id,
        "state": {},
        "test_record": {},
        "experience": ''
    }

    with open('user_data.json', 'w', encoding='utf-8-sig') as f2:  # json.dump()將資料寫成json檔案
        json.dump(user_data, f2, ensure_ascii=False, indent=4)
        f2.close()

    return '註冊完成(*´∀`)~♥'


# 聯絡老師
def Contact_Teacher():
    reply = '☀聯絡陳文玲老師' \
            '\nPN       | 06-2353535 ext. 5929' \
            '\nFAX     | 06-2370411' \
            '\nE-mail | wlc58@mail.ncku.edu.tw'
    return reply


if __name__ == '__main__':
    print(Introduction_Print())
    print(Register(user_id='1111111', text='姓名:黃淑微/學號:E94076233'))
    print(Experience(user_id='1111111', text='我的心得:巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉'))
