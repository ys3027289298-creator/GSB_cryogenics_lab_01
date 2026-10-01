import json


def new_game():
    return {'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'slots': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state):
    processed = state.setdefault("processed", set())
    element = state.get("current")
    if element in processed:
        return False
    processed.add(element)
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    target = state.get("target")
    return target is not None and target not in state.get("occupied", ())

def bug_28(state):
    return state.get("weight", -1) >= 0

def bug_5(state):
    if not state["queue"]:
        return None
    return state["queue"][0]

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
    start = state.get("start")
    end = state.get("end")
    return start is not None and end is not None and start <= end

def bug_30(state):
    if state.get("log") and state["log"][-1][1] == "failed":
        state["value"] = state["snapshot"]
        return False
    return True

def bug_31(state):
    return not state.get("settled", False)

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
