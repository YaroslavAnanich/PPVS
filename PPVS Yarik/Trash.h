#pragma once
#include "AudioFile.h"
#include<vector>

class Trash
{
public:
	int get_size();
	void add(AudioFile*);
	void clear();
private:
	vector<AudioFile*> trash;
};

