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

int BST::check(string word, node* t)
{
    int temp;
    if (word.size() < t->word.size())
    {
        temp = word.size();
    }
    else
    {
        temp = t->word.size();
    }
    for (int i = 0; i < temp; i++)
    {
        if (int(word[i]) == int(t->word[i]))
        {
            continue;
        }
        if (int(word[i]) < int(t->word[i]))
        {
            return 1;
        }
        if (int(word[i]) > int(t->word[i]))
        {
            return 2;
        }
    }
    return 3;
}

BST::node* BST::make_empty(node* t)
{
    if (t == NULL)
        return NULL;
    else
    {
        make_empty(t->left);
        make_empty(t->right);
        delete t;
    }
    return NULL;
}

BST::node* BST::push(string word, string translation, node* t)
{
    if (t == NULL)
    {
        t = new node;
        t->word = word;
        t->translation = translation;
        t->left = t->right = NULL;
        size++;
    }
    else if (check(word, t) == 1)
        t->left = push(word, translation, t->left);
    else if (check(word, t) == 2)
        t->right = push(word, translation, t->right);
    return t;
}

BST::node* BST::find_min(node* t)
{
    if (t == NULL)
        return NULL;
    else if (t->left == NULL)
        return t;
    else
        return find_min(t->left);
}

BST::node* BST::del(string word, string translation, node* t) {
    node* temp;
    if (t == NULL)
        return NULL;
    else if (check(word, t) == 1)
        t->left = del(word, translation, t->left);
    else if (check(word, t) == 2)
        t->right = del(word, translation, t->right);
    else if (t->left && t->right)
    {
        temp = find_min(t->right);
        t->word = temp->word;
        t->translation = temp->translation;
        t->right = del(word, translation, t->right);
    }
    else
    {
        temp = t;
        if (t->left == NULL)
            t = t->right;
        else if (t->right == NULL)
            t = t->left;
        delete temp;
    }
    return t;
}

BST::node* BST::find(node* t, string word) {
    if (t == NULL)
    {
        return NULL;
    }
    else if (check(word, t) == 1)
        return find(t->left, word);
    else if (check(word, t) == 2)
        return find(t->right, word);
    else
        return t;
}

void BST::print(node* t)
{
    if (t == NULL)
    {
        return;
    }
    print(t->left);
    cout << t->word << " - " << t->translation << endl;
    print(t->right);
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
    string temp1, temp2;
    int a = strlen(word);
    for (int i = 0; i < strlen(word); i++)
    {
        temp1.push_back(word[i]);
    }
    for (int i = 0; i < strlen(translation); i++)
    {
        temp2.push_back(translation[i]);
    }
    root = push(temp1, temp2, root);
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

void BST::print() {
    cout << endl;
    print(root);
    cout << endl;
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
            size++;
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