import textwrap

print()

message_key_size = input("ENTER MESSAGE / KEY SIZE:")

result_list = []

result = 1112064**int(message_key_size)

result_list.append(result)

for items in result_list:
    print()
    print("POSSIBLE COMBINATIONS OF MESSAGE WITH THIS SIZE:")
    print()
    print(textwrap.fill(str(items)))
