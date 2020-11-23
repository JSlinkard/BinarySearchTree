# Jacob Slinkard
# Binary Search Tree
# Runs a BST and allows the user to enter strings or integers for the values,
# or draw strings from a file.
# Due November 24, 2020.


# Imports
import tkinter
from tkinter.filedialog import *

# Class for node object.
class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None
		self.parent=None # pointer to parent node in tree

# Class for binary search tree.
class binary_search_tree:
	def __init__(self):
		self.root=None
        # Method for inserting a value.
	def insert(self,value):
		if self.root==None:
			self.root=node(value)
		else:
			self._insert(value,self.root)
        # Recursive insert method.
	def _insert(self,value,cur_node):
		if value<cur_node.value:
			if cur_node.left_child==None:
				cur_node.left_child=node(value)
				cur_node.left_child.parent=cur_node # set parent
			else:
				self._insert(value,cur_node.left_child)
		elif value>cur_node.value:
			if cur_node.right_child==None:
				cur_node.right_child=node(value)
				cur_node.right_child.parent=cur_node # set parent
			else:
				self._insert(value,cur_node.right_child)
		else:
			print("Value already in tree!")
        # Method for printing the values of the tree.
	def print_tree(self):
		if self.root!=None:
			self._print_tree(self.root)
        # Recursive print method.
	def _print_tree(self,cur_node):
		if cur_node!=None:
			self._print_tree(cur_node.left_child)
			print (str(cur_node.value))
			self._print_tree(cur_node.right_child)
        # Method for finding height of the tree.
	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
		else:
			return 0
        # Recursive height method.
	def _height(self,cur_node,cur_height):
		if cur_node==None: return cur_height
		left_height=self._height(cur_node.left_child,cur_height+1)
		right_height=self._height(cur_node.right_child,cur_height+1)
		return max(left_height,right_height)
        # Method for finding value.
	def find(self,value):
		if self.root!=None:
			return self._find(value,self.root)
		else:
			return None
        # Recursive find method.
	def _find(self,value,cur_node):
		if value==cur_node.value:
			return cur_node
		elif value<cur_node.value and cur_node.left_child!=None:
			return self._find(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._find(value,cur_node.right_child)
        # Method to delete a value.
	def delete_value(self,value):
		return self.delete_node(self.find(value)) 
        # Method for deleting a node.
	def delete_node(self,node):

		## -----
		# Improvements since prior lesson

		# Protect against deleting a node not found in the tree
		if node==None or self.find(node.value)==None:
			print("Node to be deleted not found in the tree!")
			return None 
		## -----

		# returns the node with min value in tree rooted at input node
		def min_value_node(n):
			current=n
			while current.left_child!=None:
				current=current.left_child
			return current

		# returns the number of children for the specified node
		def num_children(n):
			num_children=0
			if n.left_child!=None: num_children+=1
			if n.right_child!=None: num_children+=1
			return num_children

		# get the parent of the node to be deleted
		node_parent=node.parent

		# get the number of children of the node to be deleted
		node_children=num_children(node)

		# break operation into different cases based on the
		# structure of the tree & node to be deleted

		# CASE 1 (node has no children)
		if node_children==0:

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
			if node_parent!=None:
				# remove reference to the node from the parent
				if node_parent.left_child==node:
					node_parent.left_child=None
				else:
					node_parent.right_child=None
			else:
				self.root=None

		# CASE 2 (node has a single child)
		if node_children==1:

			# get the single child node
			if node.left_child!=None:
				child=node.left_child
			else:
				child=node.right_child

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
			if node_parent!=None:
				# replace the node to be deleted with its child
				if node_parent.left_child==node:
					node_parent.left_child=child
				else:
					node_parent.right_child=child
			else:
				self.root=child

			# correct the parent pointer in node
			child.parent=node_parent

		# CASE 3 (node has two children)
		if node_children==2:

			# get the inorder successor of the deleted node
			successor=min_value_node(node.right_child)

			# copy the inorder successor's value to the node formerly
			# holding the value we wished to delete
			node.value=successor.value

			# delete the inorder successor now that it's value was
			# copied into the other node
			self.delete_node(successor)
        # Method for searching for values.
	def search(self,value):
		if self.root!=None:
			return self._search(value,self.root)
		else:
			return False
        # Recursive search method.
	def _search(self,value,cur_node):
		if value==cur_node.value:
			return True
		elif value<cur_node.value and cur_node.left_child!=None:
			return self._search(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._search(value,cur_node.right_child)
		return False

# Function for opening a file.
def openFile():
    root = Tk()
    file = askopenfilename()
    items = []
    with open(file, 'r') as f:
        items = f.read().split()
    f.close()
    root.destroy()
    return items

# Main function.
def main():
    answer = 0 # Sentinel value.
    while answer != "EXIT!": # Loop until user exits.
        print("Would you like to have string or integer values?")
        answer = str(input("Enter 1 for strings, 2 for integers, or 'EXIT!' to quit: "))
        if answer == "1":
            answer = strings() # String-based tree.
        elif answer == "2":
            answer = integers() # Integer-based tree.
        elif answer == "EXIT!":
            break
        else:
            print()
            print("Please enter a valid response. '1', '2', or 'EXIT!'")

# String-based tree function.
def strings():
    tree = binary_search_tree()
    answer = "0"
    while answer != "EXIT!":
        print()
        print("Commands: 'EXIT!' to exit, 'PRINT!' to print the tree, 'OPEN!' to insert items from a file, 'SEARCH!' to search for a value in the tree, or 'DELETE!' to delete a node.")
        answer = str(input("Enter your value or a command: "))
        if answer == "EXIT!": # Exit
            return "EXIT!"
        elif answer == "PRINT!": # Print tree
            print()
            tree.print_tree()
        elif answer == "DELETE!": # Delete node
            print()
            delete = str(input("What value would you like to delete: "))
            print()
            tree.delete_value(delete)      
        elif str(answer) == "SEARCH!": # Search in tree
            print()
            search = str(input("What value would you like to search for: "))
            print()
            if tree.search(search):
                print(search + " was found.")
            else:
                print(search + " was not found.")
        elif answer == "OPEN!": # Open a file
            print()
            file = openFile()
            for line in file:
                tree.insert(line)
            print("Values from file added. ")
            
        else:
            tree.insert(answer)
# Integer-based tree function.
def integers():
    tree = binary_search_tree()
    answer = "0"
    while answer != "EXIT!":
        print()
        print("Commands: 'EXIT!' to exit, 'PRINT!' to print the tree, 'OPEN!' to insert items from a file, 'SEARCH!' to search for a value in the tree,  or 'DELETE!' to delete a node.")
        answer = input("Enter your value or a command: ")
        if str(answer) == "EXIT!": # Exit
            return "EXIT!"
        elif str(answer) == "PRINT!": # Print
            print()
            tree.print_tree()
        elif str(answer) == "DELETE!": # Delete
            print()
            delete = int(input("What value would you like to delete: "))
            print()
            tree.delete_value(delete)
        elif str(answer) == "SEARCH!": # Search
            print()
            search = int(input("What value would you like to search for: "))
            print()
            if tree.search(search):
                print(search + " was found.")
            else:
                print(search + " was not found.") 
        elif answer == "OPEN!": # Open
            print()
            file = openFile()
            for line in file:
                tree.insert(int(line))
            print("Values from file added. ")
        else:
            tree.insert(int(answer))


main()
