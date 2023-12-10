#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_LEN (int)1e6
#define MAX_VAL (int)1e3
typedef long long ll;

typedef struct node
{

    int data;
    int height;
    struct node *left_child;
    struct node *right_child;

} Node;

Node *root = NULL;
int cnt = 0;

int get_max(int a, int b)
{
    return a > b ? a : b;
}

int get_height(Node *p_node)
{
    if (p_node == NULL)
        return 0;
    else
        return p_node->height;
}

void set_height(Node *p_node)
{
    p_node->height = get_max(get_height(p_node->left_child), get_height(p_node->right_child)) + 1;
}

int get_balance_factor(Node *p_node)
{

    if (p_node == NULL)
        return 0;
    else
    {
        Node *p_left_child = p_node->left_child;
        Node *p_right_child = p_node->right_child;

        return get_height(p_left_child) - get_height(p_right_child);
    }
}

Node *LL_rotate(Node *p_node)
{

    Node *p_left_child = p_node->left_child;
    p_node->left_child = p_left_child->right_child;
    p_left_child->right_child = p_node;
    set_height(p_node);
    return p_left_child;
}

Node *RR_rotate(Node *p_node)
{

    Node *p_right_child = p_node->right_child;
    p_node->right_child = p_right_child->left_child;
    p_right_child->left_child = p_node;
    set_height(p_node);
    return p_right_child;
}

Node *LR_rotate(Node *p_node)
{
    Node *p_left_child = p_node->left_child;
    p_node->left_child = RR_rotate(p_left_child);
    set_height(p_node->left_child);
    return LL_rotate(p_node);
}

Node *RL_rotate(Node *p_node)
{

    Node *p_right_child = p_node->right_child;
    p_node->right_child = LL_rotate(p_right_child);
    set_height(p_node->right_child);
    return RR_rotate(p_node);
}

Node *balance(Node *p_node)
{

    int balance_factor = get_balance_factor(p_node);

    if (balance_factor >= 2)
    {

        if (get_balance_factor(p_node->left_child) >= 1)
        {
            p_node = LL_rotate(p_node);
        }
        else
        {
            p_node = LR_rotate(p_node);
        }
    }
    else if (balance_factor <= -2)
    {
        if (get_balance_factor(p_node->right_child) <= -1)
        {
            p_node = RR_rotate(p_node);
        }
        else
        {
            p_node = RL_rotate(p_node);
        }
    }

    set_height(p_node);

    return p_node;
}

Node *insert_node(Node *p_node, int data)
{

    if (p_node == NULL)
    {
        p_node = (Node *)malloc(sizeof(Node));
        p_node->data = data;
        p_node->height = 1;
        p_node->left_child = p_node->right_child = NULL;
    }
    else if (data < p_node->data)
    {
        p_node->left_child = insert_node(p_node->left_child, data);
        p_node = balance(p_node);
    }
    else if (data > p_node->data)
    {
        p_node->right_child = insert_node(p_node->right_child, data);
        p_node = balance(p_node);
    }
    else
    {
        printf("insert error! only unique data allowed: %d\n", data);
    }

    return p_node;
}

void print_AVL_tree(Node *p_node, int level)
{
    if (p_node == NULL)
        return;

    print_AVL_tree(p_node->right_child, level + 1);
    printf("\n");
    if (p_node == root)
    {
        printf("Root:");
    }
    else
    {
        for (int i = 0; i < level; i++)
        {
            printf("      ");
        }
    }

    printf("%d(%d)", p_node->data, get_height(p_node));
    print_AVL_tree(p_node->left_child, level + 1);
}

Node *get_min(Node *p_node)
{

    if (p_node != NULL)
    {
        if (p_node->left_child == NULL)
            return p_node;
        else
            return get_min(p_node->left_child);
    }
}

int count_child(Node *p_node)
{

    return (p_node->left_child != NULL) + (p_node->right_child != NULL);
}

Node *delete_node(Node *p_node, int data)
{

    Node *tmp = NULL;

    if (p_node == NULL)
        return NULL;
    if (data < p_node->data)
        p_node->left_child = delete_node(p_node->left_child, data);
    else if (data > p_node->data)
        p_node->right_child = delete_node(p_node->right_child, data);
    else
    {

        if (count_child(p_node) == 2)
        {
            Node *tmp = get_min(p_node->right_child);
            p_node->data = tmp->data;
            p_node->right_child = delete_node(p_node->right_child, p_node->data);
        }
        else
        {

            Node *tmp = (p_node->left_child != NULL) ? p_node->left_child : p_node->right_child;
            free(p_node);
            return tmp;
        }
    }

    p_node = balance(p_node);
    return p_node;
}