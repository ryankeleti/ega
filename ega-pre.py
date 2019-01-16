from plasTeX import Base
class unsure(Base.Command):
  args='text:str'
  def invoke(self,tex):
    Base.Command.invoke(self,tex)
class completelyunsure(Base.Command):
  args='text:str'
  def invoke(self,tex):
    Base.Command.invoke(self,tex)
class oldpage(Base.Command):
  args='text:str'
  def invoke(self,tex):
    Base.Command.invoke(self,tex)
class sref(Base.Command):
  args='text:str'
  def invoke(self,tex):
    Base.Command.invoke(self,tex)
class eref(Base.Command):
  args='text:str'
  def invoke(self,tex):
    Base.Command.invoke(self,tex)
class env(Base.Environment):
  pass
class envr(Base.Environment):
  pass

