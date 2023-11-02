#include "Album.h"

int Album::get_size()
{
	return songs.size();
}

void Album::add_file(Music* song)
{
	songs.push_back(song);
}

void Album::pop_file()
{
	songs.pop_back();
}

void Album::pop_file(Trash& trash)
{
	trash.add(songs[songs.size() - 1]);
	songs.pop_back();
}

void Album::del_file(int number)
{
	songs.erase(songs.begin() + (number - 1));
}

void Album::del_file(Trash& trash,int number)
{
	trash.add(songs[number - 1]);
	songs.erase(songs.begin() + (number - 1));
}