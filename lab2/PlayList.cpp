#include "PlayList.h"

int PlayList::get_size()
{
	return files.size();
}

void PlayList::add_file(AudioFile* file)
{
	files.push_back(file);
}

void PlayList::pop_file()
{
	files.pop_back();
}

void PlayList::pop_file(Trash& trash)
{
	trash.add(files[files.size()-1]);
	files.pop_back();
}

void PlayList::del_file(int number)
{
	files.erase(files.begin() + (number -1));
}

void PlayList::del_file(Trash& trash,int number)
{
	trash.add(files[number - 1]);
	files.erase(files.begin() + (number - 1));
}