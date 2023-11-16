#pragma once
#include <string>

using namespace std;

class AudioFile
{
public:
	void set_file_name(string file_name);
	void set_extension(string extension);
	void set_day_create(int day_create);
	void set_month_create(int month_create);
	void set_year_create(int year_create);
	string get_file_name();
	string get_extension();
	int get_day_create();
	int get_month_create();
	int get_year_create();

protected:
	string file_name;
	string extension;
	int	day_create;
	int month_create;
	int year_create;
};

