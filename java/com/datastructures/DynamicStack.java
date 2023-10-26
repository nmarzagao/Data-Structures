package com.datastructures;

import com.datastructures.Node;

public class DynamicStack {
    Node top;

    public DynamicStack() {
        this.top = null;
    }

    public DynamicStack(Node top) {
        this.top = top;
    }

    public Node getTop() {
        return this.top;
    }

    public void setTop(Node top) {
        this.top = top;
    }

    public String peek() {
        return this.top.getVal();
    }

    private boolean isEmpty() {
        return (this.top == null);
    }

    public void push(Node node) {
        if (this.isEmpty()) {
            this.top = node;
        }
        else {
            node.setNext(this.top);
            this.top = node;
        }
    }

    public String pop() {
        if (this.isEmpty()) {
            return null;
        }
        else {
            String val = this.top.getVal();
            this.top = this.top.getNext();

            return val;
        }
    }
}