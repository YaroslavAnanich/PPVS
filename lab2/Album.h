#pragma once
#include <vector>
#include "Music.h"
#include "AudioFolder.h"

class Album : public AudioFolder
{
public:
	int get_size() override;
	void add_file(Music*);
	void pop_file();
	void pop_file(Trash&);
	void del_file(int number);
	void del_file(Trash&,int number);
protected:
	vector<Music*> songs;

};

