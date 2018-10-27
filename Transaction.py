class Transaction(object):
	"""docstring for Transaction"""
	def __init__(self, sender_addr, sender_private_key, receiver_addr, ipfs_addr):
		super(Transaction, self).__init__()
		self.sender_addr = sender_addr
		self.sender_private_key = sender_private_key
		self.receiver_addr = receiver_addr
		self.ipfs_addr = ipfs_addr

	def verifyCurrOwner(self):
        """
        verify current owner before sending
        """
        private_key = RSA.importKey(binascii.unhexlify(self.sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
		