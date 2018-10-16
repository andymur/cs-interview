package com.andymur.cs.lists.tasks;


public class RevertListRunner {
    public static void main(String[] args) {
        List<String> abc = constructFromString("ABC");
        abc.print();
    }

    public static List<String> constructFromString(final String content) {
        List<String> result = new List<>();

        for (Character element: content.toCharArray()) {
            result.append(element.toString());
        }

        return result;
    }

    public static class List<E> {

        private Node<E> head = null;
        private Node<E> tail = null;

        public E append(E element) {
            assert tail == null || tail.next() == null;
            final Node<E> newTail = new Node<>(element);

            if (tail == null) {
                assert head == null;

                tail = newTail;
                head = tail;
                return element;
            }

            tail.setNext(newTail);
            tail = newTail;
            return element;
        }

        public Node<E> getHead() {
            return head;
        }

        public void print() {
            Node<E> node = head;

            if (node == null) {
                System.out.println("Empty");
                return;
            }

            System.out.println(node.element().toString());

            while (node.next() != null) {
                node = node.next();
                System.out.println(node.element().toString());
            }
        }
    }

    public static class Node<E> {
        private final E element;
        private Node<E> next = null;

        public Node(final E element) {
            assert element != null;
            this.element = element;
        }

        public void setNext(Node<E> next) {
            this.next = next;
        }

        public Node<E> next() {
            return next;
        }

        public E element() {
            return element;
        }
    }
}
