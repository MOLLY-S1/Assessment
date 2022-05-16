"""Statement formatter V1
adds decoration to important messages
"""

symbol = "*"
text = "Hello World"
sides = symbol * 5

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)




