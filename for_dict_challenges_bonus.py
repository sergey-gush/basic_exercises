"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem

from collections import Counter
import operator

def most_written_by(msgs):
    sent_by_counter = Counter(msg['sent_by'] for msg in msgs)
    return sent_by_counter.most_common(1)[0][0]

def most_replies_for(msgs):
    replies_counter = Counter(msg['reply_for'] for msg in msgs)
    replies_number = replies_counter.most_common(len(msgs))
    replies_for = {}

    for msg in replies_number:
        for it in msgs:
            if msg[0] == it['id']:
                if it['sent_by'] not in replies_for:
                    replies_for[it['sent_by']] = msg[1]
                else:
                    replies_for[it['sent_by']] += msg[1]
                break
    
    return max(replies_for.items(), key=operator.itemgetter(1))[0]

def most_seen(msgs):
    seen = {}
    
    for msg in msgs:
        if msg['sent_by'] not in seen:
            seen[msg['sent_by']] = len(msg['seen_by'])
        else:
            seen[msg['sent_by']] += len(msg['seen_by'])

    return max(seen.items(), key=operator.itemgetter(1))[0]

def prime_time(msgs):
    day_stat = {
        'утро': 0,
        'день': 0,
        'вечер': 0,
        'ночь': 0
    }

    for msg in msgs:
        if 0 <= msg['sent_at'].hour < 6:
            day_stat['ночь'] += 1
        elif 6 <= msg['sent_at'].hour < 12:
            day_stat['утро'] += 1
        elif 12 <= msg['sent_at'].hour < 18:
            day_stat['день'] += 1
        else:
            day_stat['вечер'] += 1

    return max(day_stat.items(), key=operator.itemgetter(1))[0]

def most_long_thread(msgs):
    re_msgs = []
    
    for msg in msgs:
        if msg['reply_for'] is not None:
            re_msgs.append(msg)
    
    replies_counter = Counter(msg['reply_for'] for msg in re_msgs)
    return replies_counter.most_common(1)[0][0]

def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

messages = generate_chat_history()

print(f'Больше всего сообщений написал пользователь: {most_written_by(messages)}')
print(f'Больше всего отвечали на сообщения пользователя: {most_replies_for(messages)}')
print(f'Больше всего просмотров у сообщений пользователя: {most_seen(messages)}')
print(f'Больше всего сообщений поступило за {prime_time(messages)}')
print(f'Самый длинный тред у сообщения: {most_long_thread(messages)}')


# if __name__ == "__main__":
#    print(generate_chat_history())
