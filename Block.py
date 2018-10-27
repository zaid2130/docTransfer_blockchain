class Block(object):
	"""docstring for Block"""
	def __init__(self):
		super(Block, self).__init__()
		self.transaction = []



	def doc_transfer():
		sender_addr = raw_input(Sender Address)
		receiver_addr = raw_input(Receiver Address)
		doc_addr = raw_input(Enter Document address) 
		transaction = Transaction(sender_addr, receiver_addr, doc_addr)
		self.transaction.append(transaction)

	def checkValidOwner(sender_addr):
		"""
		take value from db
		"""
		if(sender_addr == db_sender_addr):
			return true
		else:
			return false

	



		