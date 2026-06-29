def greet(name: str, greeting: str) -> str:
    return f"{greeting}, {name}"

def log_event(event: str, *tags: str, **metadata) -> None:
    print(f"Event: {event}")
    print(f"Tags: {tags}")
    print(f"MetaData: {metadata}")

greetings = greet(12, "Assalamu alaikum")
print(greetings)

log_event("login", "tag1", "tag2", "tag3", userid = 102, address = "ctg")

def create_user (name: str, *, role:str = "viewer") -> dict:
    return {"name": name, "role": role}

print(create_user('Tahmid', role="CTO"))

nums = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda v : v % 2 == 0, nums))
print(even)