#pragma once
#include"AudioFolder.h"
class AudioPlayer
{
public:
	bool play(AudioFolder*);
	bool play(AudioFile*);
};

