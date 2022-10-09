from datetime import datetime
import gc
from random import randint


#TOKEN:

class Token:
  def __init__(self, block):
    x = len(tokens_list)
    self.id = 0 if x < 1 else x
    self.creation_date = block.creation_date
    self.owner = None
    return None

  def __repr__(self):
    return f"Id: {self.id}, Creation Date: {self.creation_date}, Owner ID: {self.owner.id}"

  def has_owner(self):
    return True if self.owner is not None else False

tokens_list = []


#WALLET:

class Wallet:
  def __init__(self):
    x = len(wallets_list)
    self.id = 0 if x < 1 else x
    self.creation_date = datetime.now()
    self.tokens_owned = []
    return None

  def __repr__(self):
    return f"Id: {self.id}, Creation Date: {self.creation_date}, Tokens Owned: {len(self.tokens_owned)}"

  def has_tokens(self):
    return True if len(self.tokens_owned) != 0 else False

wallets_list = []

for i in range(20):
  w = Wallet()
  wallets_list.append(w)



#BLOCK:

class Block:
  def __init__(self, chain, subChain, nb_blocks, rec_sub):
    x = len(chain.blocks)
    self.id = 0 if x < 1 else x
    self.creation_date = datetime.now()
    self.name = 'Block ' + str(self.id)
    self.prev = self.id - 1 if self.id > 0 else None
    self.next = None
    self.token = Token(self)
    tokens_list.append(self.token)
    self.token.owner = wallets_list[int(randint(0, len(wallets_list) - 1))]
    self.token.owner.tokens_owned.append(self)
    self.parent_chain = chain
    if subChain is not None:
      self.chain = Blockchain(None, self.parent_chain, nb_blocks, rec_sub)
      self.chain.id = len(blockchains) - 1
      self.chain.subchain_id = self.chain.id - 1
      self.chain.creation_date = self.creation_date
      self.chain.name = 'Subchain ' + str(self.chain.subchain_id)
      self.chain.prev = self.chain.id - 1 if self.chain.id > 0 else None
      self.chain.next = None
    else: 
      self.chain = None
    return None

  def __repr__(self):
    msg = f"Id : {self.id}, Creation Date: {self.creation_date}, Name: {self.name}, Previous: {self.prev}, Next: {self.next}, Parent chain: {self.parent_chain.id}"
    if self.chain is not None:
      msg += f"\nSubchain: {self.chain}"
    return msg

  def is_subchain(self):
    return True if self.chain is not None else None



#NEW BLOCK:

class New_Block:
  def __init__(self, chain, subChain, x, y):
    if subChain is not None:
      self.newBlock = Block(chain, 1, x, y)
    else:
      self.newBlock = Block(chain, None, x, y)
    chain.blocks.append(self.newBlock)
    if self.newBlock.prev is not None:
      chain.blocks[self.newBlock.prev].next = self.newBlock.id
    return None

  def _check(self, chain):
    return True if chain.blocks[self.newBlock.prev].next == self.newBlock.id else False



#BLOCKCHAIN:

blockchains = []

class Blockchain:
  def __init__(self, multiChain, parent_chain, x, y):
    blockchains.append(self)
    self.blocks = []
    self.id = len(blockchains) - 1
    self.nom = 'Blockchain ' + str(self.id)
    for i in range(x):
      if i % y == 0 and multiChain is not None:
        b = New_Block(self, 1, x, y)
      else:
        i = New_Block(self, None, x, y)
    return None

  def count_blocks(self):
    return len(self.blocks)

  def print_blockchain(self):
    for block in self.blocks:
      print(block.__repr__())
    return None

  def print_subchains(self):
    for block in self.blocks:
      if block.chain is not None:
        print(f"\n{block.chain.name}: {block.chain.count_blocks()} Blocks\n")
        print(block.chain.print_blockchain())
    return None


def create_blockckain():
  try:
    x = int(input('\nNumber of Blocks: '))
  except Exception:
    x = 20
  try:
    y = int(input('\nRecurrence of the subchains: '))
    if y not in range(1, x):
      y = x + 1
  except Exception:
    y = x + 1
  Main = Blockchain(1, None, x, y)
  print(f"\nMain Blockchain: {Main.count_blocks()} Blocks\n")
  Main.print_blockchain()
  print('\nSubchains:')
  print(f"{Main.print_subchains()}\n\n")
  return None



#TRANSFER OF TOKENS:

class Transfer:
  def __init__(self, sender, receiver, nbTokens):
    self.sender = sender
    self.receiver = receiver
    self.nbTokens = nbTokens
    x = len(self.sender.tokens_owned)
    y = len(self.receiver.tokens_owned)
    if (x < self.nbTokens):
      print('Not enough Tokens on the wallet.')
      self.success = False
      return None
    z = 0
    for i in range(self.nbTokens):
      if i <= len(self.sender.tokens_owned) -1:
        self.sender.tokens_owned[i].owner = self.receiver
        self.receiver.tokens_owned.append(self.sender.tokens_owned[i])
        self.sender.tokens_owned.remove(self.sender.tokens_owned[0])
        z += 1
    if z < 1:
      print('No money send.')
      return None
    self.transfer_date = datetime.now()
    x_ = len(self.sender.tokens_owned)
    y_ = len(self.receiver.tokens_owned)
    if (x_ == x - z and y_ == y + z):
      print('Transfer successful!')
      self.success = True
      return None
    print('An error occurred :(')
    return None

  def is_success(self):
    return True if self.success == True else False

  def __repr__(self):
    return f"Sender: {self.sender.id}, Receiver: {self.receiver.id}, Number of Tokens: {self.nbTokens}\n"

def multi_transfer():
  for i in wallets_list:
    if len(i.tokens_owned) > 0:
      t = Transfer(i, wallets_list[int(randint(0, len(wallets_list) - 1))], int(randint(0, len(i.tokens_owned))))
      print(t.__repr__())
    else:
      print('No money on this wallet!\n')
  print('\n')
  return None



#SUBSIDIARY FUNCTIONS:

def introduction():
  print('\nHi! In this program, you will be able to create a two-dimensional blockchain, where a block of the main chain can itself be one.')
  print('You will have to feed the program two inputs:')
  print('The first one will be x, the number of blocks in the main chain;')
  print('The second one will be y, the occurence of the subchains.')
  print('A block will be a subchain when the id of the block mined is a multiple of y, and a subchain will contain the same number of blocks as the main one.\n')
  print('Each block mines a token, randomly attributed to a wallet.')
  print('Finally, after the blockchain is created, each wallet will randomly send a number of its tokens to another one.')
  return None

def print_wallets():
  print('WALLETS:\n')
  for i in gc.get_objects():
    if isinstance(i, Wallet):
      print(i.__repr__())
  print('\n')
  return None

def print_tokens():
  print('TOKENS:\n')
  for i in gc.get_objects():
    if isinstance(i, Token):
      print(i.__repr__())
  print('\n')
  return None



#MAIN:

def main():
  introduction()
  __BLOCKCHAIN__ = create_blockckain()
  print_tokens()
  print_wallets()
  multi_transfer()
  print_wallets()
  return None


main()
