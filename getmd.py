import html2text as ht
md_text = open('C:\\Users\\Cinvy\\Desktop\\Compose中的remember和mutableStateOf-一一网络.html', 'r', encoding='utf-8').read()

markdown = ht.html2text(md_text)

with open('make2.md', 'w', encoding='utf-8') as file:
    
    file.write(markdown)