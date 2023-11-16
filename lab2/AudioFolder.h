#pragma once
#include<vector>
#include"AudioFile.h"
#include"Trash.h"
 
using namespace std;

class AudioFolder
{
public:
	virtual int get_size() = 0;
	virtual void add_file(AudioFile*);
	virtual void pop_file() = 0;
	virtual void del_file(int number) = 0;
};

