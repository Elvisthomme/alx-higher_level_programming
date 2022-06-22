#!/usr/bin/python3
"""SinglyLinkedList module"""


class Node:
    """Node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data of node class"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """next node of the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) == Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        """Simple instantiation of SinglyLinkedList class"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position"""
        node = Node(value)
        head = self.__head
        if head is None:
            self.__head = node
        elif head.data >= value:
            node.next_node = head
            self.__head = node
        else:
            while head.next_node is not None\
              and head.next_node.data <= value:
                head = head.next_node
            if head.next_node is None:
                head.next_node = node
            else:
                node.next_node = head.next_node
                head.next_node = node
                    

    def __str__(self):
        """string representation of SinglyLinkedList"""
        head = self.__head
        if head is None:
            return ''
        else:
            string = ''
            while head is not None:
                string += str(head.data) + '\n'
                head = head.next_node
        return string[:-1]

