import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
  
  def setUp(self):
    self.__BST = Binary_Search_Tree()

	
  def test_empty_tree(self):	
    self.assertEqual('[ ]', str(self.__BST), 'Empty tree should print as "[ ]"')
  def test_in_order_zero(self):
    self.assertEqual('[ ]', str(self.__BST.in_order()), 'Empty tree should print as "[ ]"')
  def test_pre_order_zero(self):
    self.assertEqual('[ ]', str(self.__BST.pre_order()), 'Empty tree should print as "[ ]"')
  def test_post_order_zero(self):
    self.assertEqual('[ ]', str(self.__BST.post_order()), 'Empty tree should print as "[ ]"')
  def test_get_height_zero(self):
    self.assertEqual(0, self.__BST.get_height())
	
  def test_in_order_one(self):
    self.__BST.insert_element(5)
    self.assertEqual('[ 5 ]', str(self.__BST.in_order()))
  def test_pre_order_one(self):
    self.__BST.insert_element(5)
    self.assertEqual('[ 5 ]', str(self.__BST.pre_order()))
  def test_post_order_one(self):
    self.__BST.insert_element(5)
    self.assertEqual('[ 5 ]', str(self.__BST.post_order()))
  def test_get_height_one(self):
    self.__BST.insert_element(5)
    self.assertEqual(1, self.__BST.get_height())
	
  def test_in_order_two(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.assertEqual('[ 5, 7 ]', str(self.__BST.in_order()))
  def test_pre_order_two(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.assertEqual('[ 5, 7 ]', str(self.__BST.pre_order()))
  def test_post_order_two(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.assertEqual('[ 7, 5 ]', str(self.__BST.post_order()))
  def test_get_height_two(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.assertEqual(2, self.__BST.get_height())
	
  def test_in_order_three(self):
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.assertEqual('[ 3, 5, 7 ]', str(self.__BST.in_order()))
  def test_pre_order_three(self):
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.assertEqual('[ 5, 3, 7 ]', str(self.__BST.pre_order()))
  def test_post_order_three(self):
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.assertEqual('[ 3, 7, 5 ]', str(self.__BST.post_order()))
  def test_get_height_three(self):
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.assertEqual(2, self.__BST.get_height())
	
  def test_in_order_four(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.insert_element(9)
    self.assertEqual('[ 3, 5, 7, 9 ]', str(self.__BST.in_order()))
  def test_pre_order_four(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.insert_element(9)
    self.assertEqual('[ 5, 3, 7, 9 ]', str(self.__BST.pre_order()))
  def test_post_order_four(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.insert_element(9)
    self.assertEqual('[ 3, 9, 7, 5 ]', str(self.__BST.post_order()))
  def test_get_height_four(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.insert_element(9)
    self.assertEqual(3, self.__BST.get_height())
		
  def test_in_order_five(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.insert_element(9)
    self.__BST.insert_element(11)
    self.assertEqual('[ 3, 5, 7, 9, 11 ]', str(self.__BST.in_order()))
  def test_pre_order_five(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.insert_element(9)
    self.__BST.insert_element(11)
    self.assertEqual('[ 5, 3, 9, 7, 11 ]', str(self.__BST.pre_order()))
  def test_post_order_five(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.insert_element(9)
    self.__BST.insert_element(11)
    self.assertEqual('[ 3, 7, 11, 9, 5 ]', str(self.__BST.post_order()))
  def test_get_height_five(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.insert_element(9)
    self.__BST.insert_element(11)
    self.assertEqual(3, self.__BST.get_height())
	
  def test_in_order_duplicate(self):
    with self.assertRaises(ValueError):
      self.__BST.insert_element(2)
      self.__BST.insert_element(1)
      self.__BST.insert_element(3)
      self.__BST.insert_element(1)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__BST.in_order()))
  def test_pre_order_duplicate(self):
    with self.assertRaises(ValueError):
      self.__BST.insert_element(2)
      self.__BST.insert_element(1)
      self.__BST.insert_element(3)
      self.__BST.insert_element(1)
    self.assertEqual('[ 2, 1, 3 ]', str(self.__BST.pre_order()))
  def test_post_order_duplicate(self):
    with self.assertRaises(ValueError):
      self.__BST.insert_element(2)
      self.__BST.insert_element(1)
      self.__BST.insert_element(3)
      self.__BST.insert_element(1)
    self.assertEqual('[ 1, 3, 2 ]', str(self.__BST.post_order()))
  def test_get_height_duplicate(self):
    with self.assertRaises(ValueError):
      self.__BST.insert_element(2)
      self.__BST.insert_element(1)
      self.__BST.insert_element(3)
      self.__BST.insert_element(1)
    self.assertEqual(2, self.__BST.get_height())
	

  def test_in_order_empty(self):
    self.__BST.remove_element(5)
    self.assertEqual('[ ]', str(self.__BST.in_order()))
  def test_pre_order_empty(self):
    self.__BST.remove_element(5)
    self.assertEqual('[ ]', str(self.__BST.pre_order()))
  def test_post_order_empty(self):
    self.__BST.remove_element(5)
    self.assertEqual('[ ]', str(self.__BST.post_order()))
  def test_get_height_empty(self):
    self.__BST.remove_element(5)
    self.assertEqual(0, self.__BST.get_height())
	
  def test_in_order_remove_one_no_children(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.remove_element(7)
    self.assertEqual('[ 3, 5 ]', str(self.__BST.in_order()))
  def test_pre_order_remove_one_no_children(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.remove_element(7)
    self.assertEqual('[ 5, 3 ]', str(self.__BST.pre_order()))
  def test_post_order_remove_one_no_children(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.remove_element(7)
    self.assertEqual('[ 3, 5 ]', str(self.__BST.post_order()))
  def test_get_height_remove_one_no_children(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(3)
    self.__BST.remove_element(7)
    self.assertEqual(2, self.__BST.get_height())
    
  def test_in_order_remove_one_child(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(3)
    self.__BST.insert_element(7)
    self.__BST.insert_element(9)
    self.__BST.remove_element(7)
    self.assertEqual('[ 3, 5, 9 ]', str(self.__BST.in_order()))
  def test_pre_order_remove_one_child(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(3)
    self.__BST.insert_element(7)
    self.__BST.insert_element(9)
    self.__BST.remove_element(7)
    self.assertEqual('[ 5, 3, 9 ]', str(self.__BST.pre_order()))
  def test_post_order_remove_one_child(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(3)
    self.__BST.insert_element(7)
    self.__BST.insert_element(9)
    self.__BST.remove_element(7)
    self.assertEqual('[ 3, 9, 5 ]', str(self.__BST.post_order()))
  def test_get_height_remove_one_child(self):
    self.__BST.insert_element(5)
    self.__BST.insert_element(3)
    self.__BST.insert_element(7)
    self.__BST.insert_element(9)
    self.__BST.remove_element(7)
    self.assertEqual(2, self.__BST.get_height())
		
  def test_in_order_remove_two_children(self):
    self.__BST.insert_element(4)
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(6)
    self.__BST.insert_element(8)
    self.__BST.remove_element(7)
    self.assertEqual('[ 4, 5, 6, 8 ]', str(self.__BST.in_order()))
  def test_pre_order_from_two_children(self):
    self.__BST.insert_element(4)
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(6)
    self.__BST.insert_element(8)
    self.__BST.remove_element(7)
    self.assertEqual('[ 5, 4, 8, 6 ]', str(self.__BST.pre_order()))
  def test_post_order_from_two_children(self):
    self.__BST.insert_element(4)
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(6)
    self.__BST.insert_element(8)
    self.__BST.remove_element(7)
    self.assertEqual('[ 4, 6, 8, 5 ]', str(self.__BST.post_order()))
  def test_get_height_from_two_children(self):
    self.__BST.insert_element(4)
    self.__BST.insert_element(5)
    self.__BST.insert_element(7)
    self.__BST.insert_element(6)
    self.__BST.insert_element(8)
    self.__BST.remove_element(7)
    self.assertEqual(3, self.__BST.get_height())
				
  def test_in_order_after_remove(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.remove_element(15)
    self.__BST.insert_element(17)
    self.__BST.insert_element(19)
    self.__BST.insert_element(15)
    self.assertEqual('[ 5, 10, 15, 17, 19 ]', str(self.__BST.in_order()))
  def test_pre_order_after_remove(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.remove_element(15)
    self.__BST.insert_element(17)
    self.__BST.insert_element(19)
    self.__BST.insert_element(15)
    self.assertEqual('[ 10, 5, 17, 15, 19 ]', str(self.__BST.pre_order()))
  def test_post_order_after_remove(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.remove_element(15)
    self.__BST.insert_element(17)
    self.__BST.insert_element(19)
    self.__BST.insert_element(15)
    self.assertEqual('[ 5, 15, 19, 17, 10 ]', str(self.__BST.post_order()))
  def test_get_height_after_remove(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.remove_element(15)
    self.__BST.insert_element(17)
    self.__BST.insert_element(19)
    self.__BST.insert_element(15)
    self.assertEqual(3, self.__BST.get_height())
    
  def test_rotate_left_right_in_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(5)
    self.__BST.insert_element(15)
    self.__BST.insert_element(13)
    self.__BST.insert_element(17)
    self.__BST.insert_element(11)
    self.assertEqual('[ 5, 10, 11, 13, 15, 17 ]', str(self.__BST.in_order()))
  def test_rotate_left_right_pre_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(5)
    self.__BST.insert_element(15)
    self.__BST.insert_element(13)
    self.__BST.insert_element(17)
    self.__BST.insert_element(11)
    self.assertEqual('[ 13, 10, 5, 11, 15, 17 ]', str(self.__BST.pre_order()))  
  def test_rotate_left_right_post_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(5)
    self.__BST.insert_element(15)
    self.__BST.insert_element(13)
    self.__BST.insert_element(17)
    self.__BST.insert_element(11)
    self.assertEqual('[ 5, 11, 10, 17, 15, 13 ]', str(self.__BST.post_order()))   
  def test_rotate_left_right_to_list(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(5)
    self.__BST.insert_element(15)
    self.__BST.insert_element(13)
    self.__BST.insert_element(17)
    self.__BST.insert_element(11)
    self.assertEqual('[5, 10, 11, 13, 15, 17]', str(self.__BST.to_list()))
  def test_get_height_left_right_to_list(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(5)
    self.__BST.insert_element(15)
    self.__BST.insert_element(13)
    self.__BST.insert_element(17)
    self.__BST.insert_element(11)  
    self.assertEqual(3, self.__BST.get_height())
    
  def test_rotate_right_left_in_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.insert_element(4)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual('[ 4, 5, 7, 8, 10, 15 ]', str(self.__BST.in_order())) 
  def test_rotate_right_left_pre_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.insert_element(4)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual('[ 7, 5, 4, 10, 8, 15 ]', str(self.__BST.pre_order()))
  def test_rotate_right_left_post_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.insert_element(4)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual('[ 4, 5, 8, 15, 10, 7 ]', str(self.__BST.post_order())) 
  def test_rotate_right_left_to_list(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.insert_element(4)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual('[4, 5, 7, 8, 10, 15]', str(self.__BST.to_list())) 
  def test_get_height_rotate_right_left(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(15)
    self.__BST.insert_element(5)
    self.__BST.insert_element(4)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual(3, self.__BST.get_height())
    
  def test_rotate_right_right_in_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(6)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual('[ 3, 5, 6, 7, 8, 10 ]', str(self.__BST.in_order())) 
  def test_rotate_right_right_pre_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(6)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual('[ 5, 3, 7, 6, 10, 8 ]', str(self.__BST.pre_order()))
  def test_rotate_right_right_post_order(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(6)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual('[ 3, 6, 8, 10, 7, 5 ]', str(self.__BST.post_order())) 
  def test_rotate_right_right_to_list(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(6)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual('[3, 5, 6, 7, 8, 10]', str(self.__BST.to_list())) 
  def test_get_height_rotate_right_right(self):
    self.__BST.insert_element(10)
    self.__BST.insert_element(3)
    self.__BST.insert_element(5)
    self.__BST.insert_element(6)
    self.__BST.insert_element(7)
    self.__BST.insert_element(8)
    self.assertEqual(3, self.__BST.get_height())
    
  def test_rotate_left_left_in_order(self):
    self.__BST.insert_element(20)
    self.__BST.insert_element(23)
    self.__BST.insert_element(10)
    self.__BST.insert_element(7)
    self.__BST.insert_element(12)
    self.__BST.insert_element(8)
    self.assertEqual('[ 7, 8, 10, 12, 20, 23 ]', str(self.__BST.in_order()))
  def test_rotate_left_left_pre_order(self):
    self.__BST.insert_element(20)
    self.__BST.insert_element(23)
    self.__BST.insert_element(10)
    self.__BST.insert_element(7)
    self.__BST.insert_element(12)
    self.__BST.insert_element(8)
    self.assertEqual('[ 10, 7, 8, 20, 12, 23 ]', str(self.__BST.pre_order()))
  def test_rotate_left_left_post_order(self):
    self.__BST.insert_element(20)
    self.__BST.insert_element(23)
    self.__BST.insert_element(10)
    self.__BST.insert_element(7)
    self.__BST.insert_element(12)
    self.__BST.insert_element(8)
    self.assertEqual('[ 8, 7, 12, 23, 20, 10 ]', str(self.__BST.post_order()))
  def test_rotate_left_left_in_order(self):
    self.__BST.insert_element(20)
    self.__BST.insert_element(23)
    self.__BST.insert_element(10)
    self.__BST.insert_element(7)
    self.__BST.insert_element(12)
    self.__BST.insert_element(8)
    self.assertEqual('[7, 8, 10, 12, 20, 23]', str(self.__BST.to_list()))
  def test_get_height_rotate_left_left(self):
    self.__BST.insert_element(20)
    self.__BST.insert_element(23)
    self.__BST.insert_element(10)
    self.__BST.insert_element(7)
    self.__BST.insert_element(12)
    self.__BST.insert_element(8)
    self.assertEqual(3, self.__BST.get_height())
    #put above but for post and pre order test

if __name__ == '__main__':
  unittest.main()

