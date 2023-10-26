package com.datastructures;

public class Node {
    String val;
    Node next;

    public Node() {
        this.val = null;
        this.next = null;
    }

    public Node(String val) {
        this.val = val;
        this.next = null;
    }

    public Node(String val, Node next) {
        this.val = val;
        this.next = next;
    }

    public String getVal() {
        return this.val;
    }

    public void setVal(String val) {
        this.val = val;
    }

    public Node getNext() {
        return this.next;
    }

    public void setNext(Node next) {
        this.next = next;
    }
}