#pragma once
#include "AudioFolder.h"

class PlayList : public AudioFolder
{
public:
	int get_size() override;
	void add_file(AudioFile*) override;
	void pop_file() override;
	void pop_file(Trash& trash);
	void del_file(int number) override;
	void del_file(Trash& trash,int number);
protected:
	vector<AudioFile*> files;
};

