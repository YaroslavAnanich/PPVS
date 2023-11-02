#include "AudioCollection.h"

int AudioCollection::get_size()
{
	return collection.size();
}

void AudioCollection::add_folder(AudioFolder* folder)
{
	collection.push_back(folder);
}

void AudioCollection::pop_folder()
{
	collection.pop_back();
}

void AudioCollection::del_folder(int number)
{
	collection.erase(collection.begin() + (number - 1));
}