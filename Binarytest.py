import unittest


def search(li,item):
  
  mid = len(li)//2
  if len(li)==0:
    return False
  if item == li[mid]:
    return True
  elif item > li[mid]:
    return search(li[mid+1:],item)
  else:
    return search(li[:mid],item)

class Binarytest(unittest.TestCase):
  
  def setUp(self):
    pass
  def tearDown(self):
    pass
  def test_testcase(self):
    list = []
    self.assertEqual(search(list,1),False)
  def test_testcase1(self):
    list = [1,2,3]
    self.assertEqual(search(list,2),True)
  def test_testcase2(self):
    list = [1,2,3]
    self.assertEqual(search(list,3),True)
  def test_testcase3(self):
    list = [1,2,3]
    self.assertEqual(search(list,1),True)

if __name__ == '__main__':
    unittest.main()