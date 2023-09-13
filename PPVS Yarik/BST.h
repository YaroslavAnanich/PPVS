#pragma once

#include<iostream>
#include<string>
#include<fstream>
#include<iomanip>

using namespace std;

class BST
{
public:
	BST();
	~BST();
	int del(string word, string translation);
	string operator[](string word);
	void push(string word, string translation);
	void push(char word[], char translation[]);
	void pull_file(string path);
	int change_translation(string word, string translation);
	void print();
	int getSize();
private:
	class node
	{
	public:
		string word;
		string translation;
		node* left;
		node* right;
	};
	int size;
	node* root;
	node* del(string word, string translation, node* t);
	int check(string word, node* t);
	node* make_empty(node* t);
	node* find_min(node* t);
	void print(node* t);
	node* push(string word, string translation, node* t);
	node* find(node* t, string word);
};