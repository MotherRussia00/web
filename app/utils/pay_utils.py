import random
from yoomoney import Client, Quickpay

from app import settings


class PayUtils:
    _client = Client(settings.TOKEN)

    @classmethod
    def create_pay_request(cls, info: dict, money=200) -> Quickpay:
        user = cls._client.account_info()
        label = f"{info}:{cls._generate_operation_id()}"

        quick_pay = Quickpay(
            receiver=user.account,
            quickpay_form="MineIce",
            targets="Поддержите сервер",
            paymentType="SB",
            label=label,
            sum=money,
            successURL=f"https://mineice.ru/donate/success/{label}"
        )
        return quick_pay

    @classmethod
    def check_operation(cls, label: str) -> bool:
        return cls._client.operation_history(label=label).operations[0].status == "success"

    @staticmethod
    def _generate_operation_id():
        return str(random.randint(1, 10000000000000000000000000000000000000000000))
