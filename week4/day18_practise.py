# Step 1: define serval different class with the same interface
class PdfDocument:
    def __init__(self,name):
        self.name = f"{name}.pdf"

    def read(self):
        print(f"Reading content from a PDF document called {self.name}.")

    def save(self):
        print(f"saving content of {self.name} in PDF format.")

class WordDocument:
    def __init__(self,name):
        self.name = f"{name}.doc"

    def read(self):
        print(f"Reading content from a Word document called {self.name}")

    def save(self):
        print(f"saving content of {self.name} in .docx format.")

class TextDocument:
    def __init__(self,name):
        self.name = f"{name}.txt"

    def read(self):
        print(f"Reading content from a Text document called {self.name}")

    def save(self):
        print(f"Saving content of {self.name} in plain text format")

# Step 2 : Creat a function that can deal with all the objects comply with "document agreement"
def process_document(documents):
    """
    A polymorphic function that can process any document object as long as it has .read() and .save() methods.
    :param documents: the list contains the names of documents

    A polymorphic function that processes a list of document objects.
    It iterates through each document, calling its .read() and .save() methods.
    :param documents: A list containing document objects (e.g., PdfDocument, WordDocument).
    :return: None

    """
    print("--- Starting Document Processing ---")
    for doc in documents:
        doc.read()
        doc.save()
        print("-"*20)

# Step 3: Creat different types of object instances,and then put them into a list.
doc_1 = PdfDocument("doc1")
doc_2 = WordDocument("doc2")
doc_3 = TextDocument("doc3")

"""
all_docs = {}
for i in range(3):
    doc_name = f"doc{i+1}"
    all_docs[doc_name]= 
"""

# Step 4: call the polymorphism function
all_docs = [doc_1,doc_2,doc_3]
print(all_docs)
process_document(all_docs)

# extension: if we create a new document type:
class HtmlDocument:
    def __init__(self,name):
        self.name = f"{name}.html"

    def read(self):
        print(f"Reading content from a Html document called {self.name}")

    def save(self):
        print(f"Saving content of {self.name} in plain text format")
"""
The beauty of polymorphism is that we don't need to modify the process_document function at all. 
We just create an instance of our new class and add it to the list.
Then,the function process_documents do not need to be modified any more.
"""
print("\n--- After adding a new document type ---")
doc_4 = HtmlDocument("doc4")
# noinspection PyTypeChecker
all_docs.append(doc_4) #

"""
doc_4的错误提示：你的代码没有运行时错误，因为它正确运用了 Python 的动态特性。
PyCharm 的警告是一个有益的静态分析提示，它基于对代码的类型推断。
最好的解决方法不是忽略警告，而是通过类型提示或继承，更明确地告诉 PyCharm 你的意图，
这样你的代码既能正确运行，又能通过静态检查，变得更加健壮和易于维护。
使用# noinspection PyTypeChecker可以临时跳过该检查

"""

process_document(all_docs)
