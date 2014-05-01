class Thingy:
  def __init__(self,value):
    self.value = value
  def showme(self):
    print "val was %s" % self.value
  def __repr__(self):
    return str(self.value)
    
class CodedByThejaException:
  def __init__(self,msg=None):
    self.msg = msg
    def __repr__(self):
      return str(self.msg)
    
def main():
  
  t = Thingy(10)
  t.showme()
  print t.value
  t.value = 20
  print t.value
  print '%s' % t
  '''
  try:
#    fin = open('haha.txt','r')
    b = [1,2,3]; c = b[3]
#    a = 1/0
#  except:
#    print 'something bad happened'
  except ZeroDivisionError:
    print 'divide by zero'
    a = -1
  except IOError:
    print 'no such file'
  except IndexError:
    print 'bad indexing'
  '''
  
  if 1==1:
    raise CodedByThejaException('1==1!')
  else:
    print 'Raising exception not successful'
  
if __name__=='__main__':
  main()
  
  

