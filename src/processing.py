from datetime import datetime


def filter_by_state(banking_transaction: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возврата банковских операций по ключу"""
    state_banking_transaction = []
    for i in banking_transaction:
        if i["state"] == state:
            state_banking_transaction.append(i)
    return state_banking_transaction


def sort_by_date(banking_transaction: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортировки банковских операций по дате"""

    return sorted(
        banking_transaction, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse
    )


list_of_dictionaries = [
    {"id": 41433829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 51428929, "state": "EXECUTED", "date": "2019-05-03T11:31:29.514464"},
    {"id": 47728829, "state": "EXECUTED", "date": "2018-01-03T18:32:29.517764"},
]

filtered_list = filter_by_state(list_of_dictionaries, state="EXECUTED")

sorted_list = sort_by_date(list_of_dictionaries, reverse=True)

print(filtered_list)
print(sorted_list)
