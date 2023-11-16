#pragma once
#include"Music.h"
class AudioBook : public AudioFile
{
public:
	void set_text(string text);
	void set_pages(int pages);
	void set_chapters(int chapters);
	string get_text();
	int get_pages();
	int get_chapters();
	void set_author(string author);
	string get_author();
protected:
	string text;
	int pages;
	int chapters;
	string author;
};

