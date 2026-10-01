import json


def new_game():
    return {'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'queue': [],
            'src': 5, 'dst': 0, 'slots': 0, 'snapshot': 5, 'value': 5,
            'log': [], 'settled': False, 'processed': set(),
            'current': 'job-0', 'booked': {0}, 'weight': -1,
            't_start': 0, 't_end': 0}

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state):
    item = state["current"]
    if item in state["processed"]:
        return False
    state["processed"].add(item)
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    return state["dst"] not in state["booked"]

def bug_28(state):
    return state["weight"] >= 0

def bug_5(state):
    queue = state["queue"]
    return queue[0] if queue else None

def bug_12(state):
    amount = 10
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_19(state):
    return state["slots"] < state["cap"]

def bug_26(state):
    start, end = state["t_start"], state["t_end"]
    return start >= 0 and end > start

def bug_30(state):
    for _op, status in state["log"]:
        if status != "ok":
            state["value"] = state["snapshot"]
            return False
    state["snapshot"] = state["value"]
    return True

def bug_31(state):
    return not state["settled"]

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
