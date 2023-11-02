#pragma once
#include "AudioFolder.h"
class AudioCollection
{
public:
	int get_size();
	void add_folder(AudioFolder*);
	void pop_folder();
	void del_folder(int number);
protected:
	vector<AudioFolder*> collection;
};

