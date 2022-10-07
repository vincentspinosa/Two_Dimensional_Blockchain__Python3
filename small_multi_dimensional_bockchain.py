class Block:
  def __init__(self, chain, subChain):
    x = len(chain.blocks)
    self.id = 0 if x < 1 else x
    self.name = 'Block ' + str(self.id)
    self.prev = self.id - 1 if self.id > 0 else None
    self.next = None
    self.parent_chain = chain
    if subChain is not None:
      self.chain = Blockchain(None, self.parent_chain)
      y = len(blockchains)
      self.chain.id = y - 1
      self.chain.name = 'Subchain ' + str(self.chain.id)
      self.chain.prev = self.chain.id - 1 if self.chain.id > 0 else None
      self.chain.next = None
      chain.subchains.append(self.chain)
    else: 
      self.chain = None
    return None

  def __repr__(self):
    if self.chain is None:
      return f"Id : {self.id}, Name: {self.name}, Previous: {self.prev}, Next: {self.next}, Parent chain: {self.parent_chain.id}"
    return f"Id : {self.id}, Name: {self.name}, Previous: {self.prev}, Next: {self.next}, Parent chain: {self.parent_chain.id} \nSubchain: {self.chain}"


class New_Block:
  def __init__(self, chain, subChain):
    if subChain is not None:
      self.newBlock = Block(chain, 1)
    else:
      self.newBlock = Block(chain, None)
    chain.blocks.append(self.newBlock)
    if self.newBlock.prev is not None:
      chain.blocks[self.newBlock.prev].next = self.newBlock.id
    return None

  def __repr__(self):
    if self.newBlock is not None:
      return True

blockchains = []

class Blockchain:
  def __init__(self, multiChain, parent_chain):
    blockchains.append(self)
    self.blocks = []
    self.id = len(blockchains) - 1
    self.nom = 'Blockchain ' + str(self.id)
    if multiChain is not None:
      self.subchains = []
    for i in range(20):
      if i % 3 == 0 and multiChain is not None:
        i = New_Block(self, 1)
        self.subchains.append(i)
      else:
        i = New_Block(self, None)
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

Main = Blockchain(1, None)

print(f"Main Blockchain: {Main.count_blocks()} Blocks\n")

Main.print_blockchain()

print('\nSubchains:')
Main.print_subchains()

print('\n')

for i in blockchains:
  print(f"{i.nom}: {i.count_blocks()} Blocks\n")
