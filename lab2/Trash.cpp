#include "Trash.h"

int Trash::get_size()
{
	return trash.size();
}

void Trash::clear()
{
	trash.clear();
}

void Trash::add(AudioFile* file)
{
	trash.push_back(file);
}