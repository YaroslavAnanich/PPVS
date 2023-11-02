#pragma once
#include "AudioFile.h"
class Vioce_Message : public AudioFile
{
public:
	void set_app(string);
	string get_app();
private:
	string applicatiton;
};

