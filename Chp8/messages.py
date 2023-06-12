messages = ["test", "test 2", "test 3"]
sent_messages = []
def send_messages(messages):
    for message in messages:
        print(message)
    while messages:
        sent_messages.append(messages.pop())

send_messages(messages[:])

print(f"messages list: {messages}")

print(f"sent_messages list: {sent_messages}")
