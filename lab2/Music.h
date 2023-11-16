#pragma once
#include"AudioFile.h"

class Music : public AudioFile
{
public:
	void set_author(string author);
	string get_author();
protected:
	string author;
};

