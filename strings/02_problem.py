#wap to fill in a letter template given below 
letter = '''Dear <|Name|> , 
you are selected!
<|Date|>'''
print(letter.replace("<|Name|>", "Navneet").replace("<|Date|>", "30 june 2026"))
