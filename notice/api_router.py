from game.enums.receive_event import ReceiveEvent
from game.api.api import bet

router = {
    ReceiveEvent.ReqBet.value: bet
}
