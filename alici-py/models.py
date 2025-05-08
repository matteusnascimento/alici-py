from database import db
from datetime import datetime


class Message(db.Model):
	__tablename__ = 'messages'
	
	id = db.Column(db.Integer, primary_key=True)  # ID da mensagem
	sender = db.Column(db.String(10))  # 'user' ou 'ai'
	content = db.Column(db.Text)  # Conteúdo da mensagem
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Data/hora da mensagem
	
	def __repr__(self):
		return f"<Message {self.id} from {self.sender}>"
