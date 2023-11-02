#include "AudioFile.h"

void AudioFile::set_file_name(string file_name)
{
	this->file_name = file_name;
}

void AudioFile::set_extension(string extension)
{
	this->extension = extension;
}

void AudioFile::set_day_create(int day_create)
{
	this->day_create = day_create;
}

void AudioFile::set_month_create(int month_create)
{
	this->month_create = month_create;
}

void AudioFile::set_year_create(int year_create)
{
	this->year_create = year_create;
}

string AudioFile::get_file_name()
{
	return file_name;
}

string AudioFile::get_extension()
{
	return extension;
}

int AudioFile::get_day_create()
{
	return day_create;
}

int AudioFile::get_month_create()
{
	return month_create;
}

int AudioFile::get_year_create()
{
	return year_create;
}