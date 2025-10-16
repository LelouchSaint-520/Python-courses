# Step 1: define serval different class with the same interface
class PdfDocument:
    def __init__(self,name):
        self.name = f"{name}.pdf"

    def read(self):
        print(f"Reading content from a PDF document called {self.name}.")
        return self.name

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
    :param documents: name of document
    :return: save or read
    """
    print("--- Starting Document Processing ---")
    for doc in documents:
        doc.read()
        doc.save()
        print("-"*20)

# Step 3: Creat different types of object instances,and then put them into a list.
doc1 = PdfDocument("doc1")
doc2 = WordDocument("doc2")
doc3 = TextDocument("doc3")

"""
all_docs = {}
for i in range(3):
    doc_name = f"doc{i+1}"
    all_docs[doc_name]= 
"""
all_docs = [doc1,doc2,doc3]
print(all_docs)
process_document(all_docs)