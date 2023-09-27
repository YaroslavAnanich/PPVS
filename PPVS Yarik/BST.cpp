#include "BST.h"

BST::BST()
{
    root = NULL;
    size = 0;
}

BST::~BST()
{
    root = make_empty(root);
}

BST::Check BST::check(string word, node* input_node)
{
    Check state;
    int length;
    if (word.size() < input_node->word.size())
    {
        length = word.size();
    }
    else
    {
        length = input_node->word.size();
    }
    for (int i = 0; i < length; i++)
    {
        if (int(word[i]) == int(input_node->word[i]))
        {
            continue;
        }
        if (int(word[i]) < int(input_node->word[i]))
        {
            return state = LESS;
        }
        if (int(word[i]) > int(input_node->word[i]))
        {
            return state = MORE;
        }
    }
    return state = EQUAL;
}

BST::node* BST::make_empty(node* input_node)
{
    if (input_node == NULL)
        return NULL;
    else
    {
        make_empty(input_node->left);
        make_empty(input_node->right);
        delete input_node;
    }
    return NULL;
}

BST::node* BST::push(string word, string translation, node* input_node)
{
    if (input_node == NULL)
    {
        input_node = new node;
        input_node->word = word;
        input_node->translation = translation;
        input_node->left = input_node->right = NULL;
        size++;
    }
    else if (check(word, input_node) == LESS)
        input_node->left = push(word, translation, input_node->left);
    else if (check(word, input_node) == MORE)
        input_node->right = push(word, translation, input_node->right);
    return input_node;
}

BST::node* BST::find_min(node* input_node)
{
    if (input_node == NULL)
        return NULL;
    else if (input_node->left == NULL)
        return input_node;
    else
        return find_min(input_node->left);
}

BST::node* BST::del(string word, string translation, node* input_node) {
    node* del_node;
    if (input_node == NULL)
        return NULL;
    else if (check(word, input_node) == LESS)
        input_node->left = del(word, translation, input_node->left);
    else if (check(word, input_node) == MORE)
        input_node->right = del(word, translation, input_node->right);
    else if (input_node->left && input_node->right)
    {
        del_node = find_min(input_node->right);
        input_node->word = del_node->word;
        input_node->translation = del_node->translation;
        input_node->right = del(word, translation, input_node->right);
    }
    else
    {
        del_node = input_node;
        if (input_node->left == NULL)
            input_node = input_node->right;
        else if (input_node->right == NULL)
            input_node = input_node->left;
        delete del_node;
    }
    return input_node;
}

BST::node* BST::find(node* input_node, string word) {
    if (input_node == NULL)
    {
        return NULL;
    }
    else if (check(word, input_node) == LESS)
        return find(input_node->left, word);
    else if (check(word, input_node) == MORE)
        return find(input_node->right, word);
    else
        return input_node;
}




string BST::operator[](string word)
{
    if (find(root, word) != NULL)
    {
        return find(root, word)->translation;
    }
}

void BST::push(string word, string translation) {
    root = push(word, translation, root);
}

void BST::push(char word[], char translation[]) {
    string push_word, push_translation;
    int a = strlen(word);
    for (int i = 0; i < strlen(word); i++)
    {
        push_word.push_back(word[i]);
    }
    for (int i = 0; i < strlen(translation); i++)
    {
        push_translation.push_back(translation[i]);
    }
    root = push(push_word, push_translation, root);
}

int BST::del(string word, string translation)
{
    if (find(root, word) != NULL)
    {
        size--;
        root = del(word, translation, root);
    }
    else
    {
        return NULL;
    }
}



int BST::getSize() { return size; }

void BST::pull_file(string path)
{
    ifstream fin;
    string word, translation;
    fin.open(path);
    if (fin.is_open())
    {
        while (!fin.eof())
        {
            word = "";
            translation = "";
            fin >> word;
            fin >> translation;
            push(word, translation);
            
        }
    }
    fin.close();
}

int BST::change_translation(string word, string translation)
{
    if (find(root, word) != NULL)
    {
        find(root, word)->translation = translation;
    }
    else
    {
        return NULL;
    }
}