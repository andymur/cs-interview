package com.andymur.cs.lists.tasks;


public class RevertListRunner {

    public static void main(String[] args) {
        List<String> abc = constructFromString("ABC");
        List<String> cba = reverseList(abc);
        abc.print();
        cba.print();
    }

    public static List<String> constructFromString(final String content) {
        List<String> result = new List<>();

        for (Character element: content.toCharArray()) {
            result.append(element.toString());
        }

        return result;
    }

    public static <E> List<E> reverseList(List<E> originalList) {
        final List<E> result = new List<>();

        if (originalList == null) {
            return null;
        }

        if (originalList.getHead() == null) {
            return result;
        }

        if (originalList.getHead().next() == null) {
            result.append(originalList.getHead().element());
            return result;
        }

        // NULL (p) o1(c) -> o2(n) -> NULL
        // NULL <- o1(p) o2(c) -> NULL(n)
        // NULL <- o1 <- o2 NULL

        Node<E> prev = null;
        Node<E> current = originalList.getHead();
        Node<E> nxt = current.next();

        while (nxt != null) {
            current.setNext(prev);
            prev = current;
            current = nxt;
            nxt = current.next();
        }

        current.setNext(prev);

        return new List<>(current);
    }

    public static class List<E> {

        private Node<E> head = null;
        private Node<E> tail = null;

        public List() {
        }

        public List(Node<E> head) {
            this.head = head;
        }

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
