#include <stdio.h>
#include <stdlib.h>

#define BLACK 0
#define RED 1

typedef struct node
{
    int color, key;
    struct node *left, *right, *p;
} Node;

typedef struct
{
    Node *root;
    Node *nil;
} RBTree;

void init_RBTree(RBTree *T)
{
    T->nil = (Node *)malloc(sizeof(Node));

    T->nil->p = NULL;
    T->nil->left = NULL;
    T->nil->right = NULL;
    T->nil->key = 0;
    T->nil->color = BLACK;

    T->root = T->nil;
}

Node *new_node(int data)
{
    Node *tmp = malloc(sizeof(Node));

    tmp->p = NULL;
    tmp->left = NULL;
    tmp->right = NULL;
    tmp->key = data;
    tmp->color = RED;

    return tmp;
}

Node *tree_minimum(RBTree *T, Node *x)
{
    while (x->left != T->nil)
    {
        x = x->left;
    }
    return x;
}

void left_rotate(RBTree *T, Node *x)
{
    Node *y = x->right;
    x->right = y->left;
    if (y->left != T->nil)
        y->left->p = x;
    y->p = x->p;
    if (x->p == T->nil)
        T->root = y;
    else if (x == x->p->left)
        x->p->left = y;
    else
        x->p->right = y;
    y->left = x;
    x->p = y;
}

void right_rotate(RBTree *T, Node *x)
{
    Node *y = x->left;
    x->left = y->right;
    if (y->right != T->nil)
        y->right->p = x;
    y->p = x->p;
    if (x->p == T->nil)
        T->root = y;
    else if (x == x->p->left)
        x->p->left = y;
    else
        x->p->right = y;
    y->right = x;
    x->p = y;
}

void rb_insert_fixup(RBTree *T, Node *z)
{
    while (z->p->color == RED)
    {
        if (z->p == z->p->p->left)
        {
            Node *y = z->p->p->right;
            if (y->color == RED)
            {
                z->p->color = BLACK;
                y->color = BLACK;
                z->p->p->color = RED;
                z = z->p->p;
            }
            else if (z == z->p->right)
            {
                z = z->p;
                left_rotate(T, z);
            }
            else
            {
                z->p->color = BLACK;
                z->p->p->color = RED;
                right_rotate(T, z->p->p);
            }
        }
        else
        {
            Node *y = z->p->p->left;
            if (y->color == RED)
            {
                z->p->color = BLACK;
                y->color = BLACK;
                z->p->p->color = RED;
                z = z->p->p;
            }
            else if (z == z->p->left)
            {
                z = z->p;
                right_rotate(T, z);
            }
            else
            {
                z->p->color = BLACK;
                z->p->p->color = RED;
                left_rotate(T, z->p->p);
            }
        }
    }
    T->root->color = BLACK;
}

void rb_insert(RBTree *T, Node *z)
{
    Node *y = T->nil;
    Node *x = T->root;

    while (x != T->nil)
    {
        y = x;
        if (z->key < x->key)
            x = x->left;
        else
            x = x->right;
    }
    z->p = y;
    if (y == T->nil)
        T->root = z;
    else if (z->key < y->key)
        y->left = z;
    else
        y->right = z;

    z->left = T->nil;
    z->right = T->nil;
    z->color = RED;
    rb_insert_fixup(T, z);
}

void rb_transplant(RBTree *T, Node *u, Node *v)
{
    if (u->p == T->nil)
        T->root = v;
    else if (u == u->p->left)
        u->p->left = v;
    else
        u->p->right = v;
    v->p = u->p;
}

void rb_delete_fixup(RBTree *T, Node *x)
{
    while (x != T->root && x->color == BLACK)
    {
        if (x == x->p->left)
        {
            Node *w = x->p->right;
            if (w->color == RED)
            {
                w->color = BLACK;
                x->p->color = RED;
                left_rotate(T, x->p);
                w = x->p->right;
            }
            if (w->left->color == BLACK && w->right->color == BLACK)
            {
                w->color = RED;
                x = x->p;
            }
            else if (w->right->color == BLACK)
            {
                w->left->color = BLACK;
                w->color = RED;
                right_rotate(T, w);
                w = x->p->right;
            }
            else
            {
                w->color = x->p->color;
                x->p->color = BLACK;
                w->right->color = BLACK;
                left_rotate(T, x->p);
                x = T->root;
            }
        }
        else
        {
            Node *w = x->p->left;
            if (w->color == RED)
            {
                w->color = BLACK;
                x->p->color = RED;
                right_rotate(T, x->p);
                w = x->p->left;
            }
            if (w->right->color == BLACK && w->left->color == BLACK)
            {
                w->color = RED;
                x = x->p;
            }
            else if (w->left->color == BLACK)
            {
                w->right->color = BLACK;
                w->color = RED;
                left_rotate(T, w);
                w = x->p->left;
            }
            else
            {
                w->color = x->p->color;
                x->p->color = BLACK;
                w->left->color = BLACK;
                right_rotate(T, x->p);
                x = T->root;
            }
        }
    }
    x->color = BLACK;
}

void rb_delete(RBTree *T, Node *z)
{
    Node *y = z;
    Node *x;
    int y_original_color = y->color;
    if (z->left == T->nil)
    {
        x = z->right;
        rb_transplant(T, z, z->right);
    }
    else if (z->right == T->nil)
    {
        x = z->left;
        rb_transplant(T, z, z->left);
    }
    else
    {
        y = tree_minimum(T, z->right);
        y_original_color = y->color;
        x = y->right;
        if (y->p == z)
            x->p = y;
        else
        {
            rb_transplant(T, y, y->right);
            y->right = z->right;
            y->right->p = y;
        }
        rb_transplant(T, z, y);
        y->left = z->left;
        y->left->p = y;
        y->color = z->color;
    }
    if (y_original_color == BLACK)
        rb_delete_fixup(T, x);
}

void inorder(RBTree *T, Node *root)
{
    // 노드 n이 트리의 NIL이 아니면 n의 왼쪽 자식 노드를 출력 후 오른쪽 자식 노드를 출력
    if (root != T->nil)
    {
        inorder(T, root->left);
        printf("%d ", root->key);
        inorder(T, root->right);
    }
}

void print_RBTree(RBTree *T, Node *root, int depth)
{
    if (root == T->nil)
        return;

    print_RBTree(T, root->right, depth + 1);
    printf("\n");
    if (root == T->root)
    {
        printf("Root: ");
    }
    else
    {
        for (int i = 0; i < depth; i++)
            printf("    ");
    }

    printf("%d", root->key);
    if (root->color == RED)
        printf("(R)");
    else
        printf("(B)");
    print_RBTree(T, root->left, depth + 1);
}

int main()
{
    RBTree tree;
    init_RBTree(&tree);
    Node *a, *b, *c, *d, *e, *f, *g, *h, *i, *j, *k, *l, *m;
    a = new_node(13);
    b = new_node(10);
    c = new_node(15);
    d = new_node(5);
    e = new_node(7);
    //    f = new_node(11);
    rb_insert(&tree, a);
    rb_insert(&tree, b);
    rb_insert(&tree, c);
    rb_insert(&tree, d);
    rb_insert(&tree, e);
    //    rb_insert(&tree, f);

    print_RBTree(&tree, tree.root, 1);
    printf("\n\n");

    print_RBTree(&tree, tree.root, 1);
    printf("\n\n");

    return 0;
}