from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        found_category = next(x for x in self.categories if x.id == category_id)
        found_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        found_topic = next(x for x in self.topics if x.id == topic_id)
        found_topic.topic = new_topic
        found_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        found_document = next(x for x in self.documents if x.id == document_id)
        found_document.file_name = new_file_name

    def delete_category(self, category_id):
        found_category = next(x for x in self.categories if x.id == category_id)
        self.categories.remove(found_category)

    def delete_topic(self, topic_id):
        found_topic = next(x for x in self.topics if x.id == topic_id)
        self.topics.remove(found_topic)

    def delete_document(self, document_id):
        found_document = next(x for x in self.documents if x.id == document_id)
        self.documents.remove(found_document)

    def get_document(self, document_id):
        found_document = next(x for x in self.documents if x.id == document_id)
        return found_document

    def  __repr__(self):
        return '\n'.join(document.__repr__() for document in self.documents)



