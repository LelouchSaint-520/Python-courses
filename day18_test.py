
from day18_practise import PdfDocument, WordDocument, TextDocument

"""
# 先把你的类放在一个列表里
class Pdf:
    def __init__(self,name):
        self.name = name

    def read(self):
        print(f"Reading content from a PDF document called {self.name}.")
        return self.name

    def save(self):
        print(f"saving content of {self.name} in PDF format.")

class Word:
    def __init__(self,name):
        self.name = name

    def read(self):
        print(f"Reading content from a Word document called {self.name}")

    def save(self):
        print(f"saving content of {self.name} in .docx format.")

class Text:
    def __init__(self,name):
        self.name = name

    def read(self):
        print(f"Reading content from a Text document called {self.name}")

    def save(self):
        print(f"Saving content of {self.name} in plain text format")
        
        
document_classes = [Pdf, Word, Text]
"""
document_classes = [PdfDocument, WordDocument, TextDocument]
all_docs = []
for i, doc_class in enumerate(document_classes):
    # 在循环内部创建对象
    doc_name = f"doc{i + 1}"
    new_document = doc_class(doc_name)  # 例如：Pdf("doc1")

    # 将新创建的对象添加到列表
    all_docs.append(new_document)

print(all_docs)

list_even = [i*2 for i in range(101)]
print(list_even)
list_5 = [num for num in list_even  if num%5==0 ]
print(list_5)


